# Drug-induced liver injury prediction

Drug‐induced liver injury (DILI) represents a significant concern in healthcare, being the leading cause of acute liver failure and a common factor behind drug withdrawals from the market. Clinical presentations of DILI vary widely, and toxicity may manifest independent of the drug dosage. This underscores the need for robust predictive tools to assess the potential hepatotoxicity of pharmaceutical candidates.This study focuses on predicting clinically relevant DILI solely based on drug structure using binary classification methods. The results obtained serve a dual purpose, offering valuable insights for both clinical applications and early-stage drug development. In a clinical setting, these findings function as a screening tool for assessing DILI, providing healthcare professionals with a means to identify potential liver injury risks associated with specific drugs.Moreover, in the realm of drug development, these predictive outcomes aid in the identification and exclusion of potentially hepatotoxic candidates during the early stages of research and development. This proactive approach contributes to the mitigation of risks associated with drug-induced liver injury, enhancing the safety profile of pharmaceuticals entering the market and aligning with the overarching goal of delivering effective and safe therapeutics to patients.

## Identifiers

* EOS model ID: `eos7e3s`
* Slug: `dili-pred`

## Characteristics

* Input: `Compound`
* Input Shape: `Single`
* Task: `Classification`
* Output: `Probability`
* Output Type: `Float`
* Output Shape: `Single`
* Interpretation: prediction of drug-induced liver injury (DILI) based on structural and physicochemical descriptors

## References

* [Publication](https://pubmed.ncbi.nlm.nih.gov/30325042/)
* [Source Code](https://github.com/cptbern/QSAR_DILI_2019)
* Ersilia contributor: [leilayesufu](https://github.com/leilayesufu)

## Ersilia model URLs
* [GitHub](https://github.com/ersilia-os/eos7e3s)
* [AWS S3](https://ersilia-models-zipped.s3.eu-central-1.amazonaws.com/eos7e3s.zip)
* [DockerHub](https://hub.docker.com/r/ersiliaos/eos7e3s) (AMD64, ARM64)

## Citation

If you use this model, please cite the [original authors](https://pubmed.ncbi.nlm.nih.gov/30325042/) of the model and the [Ersilia Model Hub](https://github.com/ersilia-os/ersilia/blob/master/CITATION.cff).

## License

This package is licensed under a GPL-3.0 license. The model contained within this package is licensed under a None license.

Notice: Ersilia grants access to these models 'as is' provided by the original authors, please refer to the original code repository and/or publication if you use the model in your research.

## About Us

The [Ersilia Open Source Initiative](https://ersilia.io) is a Non Profit Organization ([1192266](https://register-of-charities.charitycommission.gov.uk/charity-search/-/charity-details/5170657/full-print)) with the mission is to equip labs, universities and clinics in LMIC with AI/ML tools for infectious disease research.

[Help us](https://www.ersilia.io/donate) achieve our mission!