# Drug-induced liver injury prediction

Prediction of clinically relevant drug-induced-liver-injury (DILI), based solely on drug structure using binary classification methods. The authors collected a public dataset of 475 molecules with associated DILI outcomes, and built a model with an accuracy of 0.89. The model checkpoints have not been provided so Ersilia has used the provided data to retrain the model.

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
* Interpretation: Probability that a drug causes DILI

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