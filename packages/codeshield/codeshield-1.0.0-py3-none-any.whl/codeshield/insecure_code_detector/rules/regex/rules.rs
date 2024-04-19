// (c) Meta Platforms, Inc. and affiliates. Confidential and proprietary.

use std::collections::HashMap;

use lazy_static::lazy_static;
use lsp_util::LanguageId;
use regex::Regex;
use serde::Deserialize;
use tracing::error;

#[derive(Deserialize, Debug)]
pub struct RawRule {
    pub description: String,
    pub cwe_id: String,
    pub rule: String,
    pub severity: Option<String>,
    pub pattern_id: String,
}

#[derive(Clone, Debug)]
pub struct Rule {
    pub description: String,
    pub cwe_id: String,
    pub regex: Regex,
    pub severity: Option<String>,
    pub pattern_id: String,
}

lazy_static! {
    static ref JAVASCRIPT_RULES: Vec<&'static str> = vec![
        include_str!("javascript.yaml"),
        include_str!("internal/javascript.yaml"),
        include_str!("language_agnostic.yaml"),
    ];

    static ref RULES: HashMap<LanguageId, Vec<Rule>> = {
        let sources = HashMap::from([
            (
                LanguageId::C,
                vec![
                    include_str!("c.yaml"),
                    include_str!("internal/c.yaml"),
                    include_str!("language_agnostic.yaml"),
                ],
            ),
            (LanguageId::Cpp,
                vec![
                    include_str!("cpp.yaml"),
                    include_str!("c.yaml"),
                    include_str!("internal/c.yaml"),
                    include_str!("language_agnostic.yaml"),
                ],
            ),
            // Csharp not supported in CodeCompose yet
            // (LanguageId::Csharp,
            //     vec![
            //         include_str!("csharp.yaml"),
            //         include_str!("internal/csharp.yaml"),
            //         include_str!("language_agnostic.yaml"),
            //     ],
            // ),
            (
                LanguageId::Hack,
                vec![
                    include_str!("internal/hack.yaml"),
                    include_str!("hack.yaml"),
                    include_str!("php.yaml"),
                    include_str!("language_agnostic.yaml"),
                ],
            ),
            (
                LanguageId::Java,
                vec![
                    include_str!("java.yaml"),
                    include_str!("internal/java.yaml"),
                    include_str!("language_agnostic.yaml"),
                ],
            ),
            (
                LanguageId::Javascript,
                JAVASCRIPT_RULES.to_vec(),
            ),
            (
                LanguageId::Javascriptreact,
                JAVASCRIPT_RULES.to_vec(),
            ),
            (
                LanguageId::Typescript,
                JAVASCRIPT_RULES.to_vec(),
            ),
            (
                LanguageId::Typescriptreact,
                JAVASCRIPT_RULES.to_vec(),
            ),
            (
                LanguageId::Flow,
                JAVASCRIPT_RULES.to_vec(),
            ),
            (
                LanguageId::Objectivec,
                vec![
                    include_str!("objective_c.yaml"),
                    include_str!("c.yaml"),
                    include_str!("internal/c.yaml"),
                    include_str!("language_agnostic.yaml"),
                ],
            ),
            (
                LanguageId::Python,
                vec![
                    include_str!("python.yaml"),
                    include_str!("internal/python.yaml"),
                    include_str!("language_agnostic.yaml"),
                ],
            ),
        ]);
        sources
            .into_iter()
            .map(|(l, ss)| {
                let rules = ss
                    .iter()
                    .flat_map(|s| {
                        let raw_rules: Vec<RawRule> =
                            match serde_yaml::from_str(s) {
                                Ok(r) => r,
                                Err(e) => {
                                    // If a language yaml import starts failing, you can change the `error!("Failed to parse YAML: {}", e);` line
                                    // to use `println!` instead, which will let you see the issue when running unit tests
                                    // However, in production, error! *must* be used since the CodeCompose LSP needs this stderr format to run correctly
                                    error!("Failed to parse YAML: {}", e);
                                    vec![]
                                }};
                        raw_rules
                            .iter()
                            .map(|r| Rule {
                                description: r.description.clone(),
                                cwe_id: r.cwe_id.clone(),
                                regex: Regex::new(&r.rule).unwrap(),
                                severity: r.severity.clone(),
                                pattern_id: r.pattern_id.clone(),
                            })
                            .collect::<Vec<Rule>>()
                    })
                    .collect::<Vec<Rule>>();
                (l, rules)
            })
            .collect::<HashMap<LanguageId, Vec<Rule>>>()
    };
}

pub fn get_insecure_regex_rules() -> &'static HashMap<LanguageId, Vec<Rule>> {
    &RULES
}

#[cfg(test)]
mod tests {
    use std::collections::HashSet;

    use super::*;

    #[test]
    fn test_rules_cpp() {
        assert_eq!(
            RULES.get(&LanguageId::Cpp).unwrap()[0].description,
            "Uses deprecated auto_ptr, which can lead to undefined behavior."
        );
        assert_eq!(RULES.get(&LanguageId::Cpp).unwrap()[0].cwe_id, "CWE-665");
        assert_eq!(
            RULES.get(&LanguageId::Cpp).unwrap()[0].pattern_id,
            "bugprone-scanf"
        );

        assert!(
            (Regex::new("\\bstd::auto_ptr").unwrap()).is_match("std::auto_ptr<int> i(new int(1));")
        );
        let example_regex = &RULES.get(&LanguageId::Cpp).unwrap()[0].regex;
        assert_eq!(
            example_regex.as_str(),
            Regex::new(r"\bstd::auto_ptr<\s*\w+\s*>").unwrap().as_str(),
        );
        assert!(example_regex.is_match("std::auto_ptr<int> i(new int(1));"));
    }

    #[test]
    fn test_rules_c() {
        assert_eq!(
            RULES.get(&LanguageId::C).unwrap()[0].regex.as_str(),
            r#"\bscanf\s*\(\s*"[^"]*%s[^"]*"[^)]*\)"#
        );
    }

    #[test]
    fn test_rules_hack() {
        assert_eq!(
            RULES.get(&LanguageId::Hack).unwrap()[0].regex.as_str(),
            r#".*<m:script>.*|.*<unsafe-raw-script-POTENTIAL-XSS-HOLE>.*"#
        );

        // make sure escaped ( is matching correctly
        assert!(
            RULES.get(&LanguageId::Hack).unwrap()[1]
                .regex
                .is_match("/actionUpdateAndAddAdmin("),
        );
    }

    #[test]
    fn test_no_new_rules() {
        let languages_imported: HashSet<LanguageId> = RULES.keys().cloned().collect();
        let languages_expected: HashSet<LanguageId> = [
            LanguageId::C,
            LanguageId::Cpp,
            // Csharp not supported in CodeCompose yet
            // LanguageId::Csharp,
            LanguageId::Flow,
            LanguageId::Hack,
            LanguageId::Java,
            LanguageId::Javascript,
            LanguageId::Javascriptreact,
            LanguageId::Objectivec,
            LanguageId::Python,
            LanguageId::Typescript,
            LanguageId::Typescriptreact,
        ]
        .iter()
        .cloned()
        .collect();
        assert_eq!(
            languages_imported, languages_expected,
            "If adding a new language, please update language_expected to verify that the regex file is actually read in correctly. Otherwise you may break the CodeCompose LSP (D50748873 for context)",
            // If a language yaml import starts failing, you can change the `error!("Failed to parse YAML: {}", e);` line
            // to use `println!` instead, which will let you see the issue when running unit tests
            // However, in production, error! *must* be used since the CodeCompose LSP needs this stderr format to run correctly
        );

        for language in languages_expected {
            assert!(
                !RULES.get(&language).unwrap().is_empty(),
                "{language} was unable to import any rules"
            );
        }
    }
}
