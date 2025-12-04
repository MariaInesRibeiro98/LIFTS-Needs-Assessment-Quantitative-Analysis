# LIFTS Needs Assessment: Quantitative Analysis

This repository contains the quantitative analysis code and scripts of the LIFTS Needs Assessment study. The analysis focuses on structuring and validation of physical activity (PA) determinants identified through participatory research with adolescents with mild intellectual disability in Dutch practical education schools.

The repository implements:
- **Structuring analysis**: Hierarchical clustering of PA determinants based on adolescents' importance ratings, demographic subgroup comparisons (gender and age groups), and within-group agreement analysis
- **Validation analysis**: Fleiss' Kappa inter-rater agreement analysis of categorical quiz responses to validate researcher interpretations and assess consensus among adolescents

## LIFTS Project Context

This research was conducted as part of the "Healthy Lifestyle for low liTerate teenagerS" (LIFTS) project (2023-2028), which promotes healthy lifestyles among adolescents with mild ID in Dutch PrO schools. LIFTS targets three health domains: PA, nutrition and mental well-being. Formative research is needed to identify behavioral determinants and adapt digital interventions to this population and context. This study addresses the PA component of this formative research phase.

## Article submitted and under review

## Title 

Physical Activity Determinants Among Adolescents With Mild Intellectual Disability in Dutch Practical Education

## Abstract

A sedentary lifestyle is a global health crisis, contributing to chronic disease and premature mortality. Adolescents with mild intellectual disability (ID) attending Dutch practical education (PrO) schools face elevated health risks due to low physical activity (PA) levels and limited conceptual, social, and practical skills. Digital health interventions offer scalable solutions but require contextual adaptation informed by formative research, addressing gaps in theoretical rigor, accessible participatory approaches and multi-stakeholder triangulation.

**Objective:** To identify PA determinants among adolescents with mild ID in Dutch PrO schools, using a theory-driven, participatory and multi-stakeholder approach to inform the contextual adaptation of digital health interventions.

**Methods:** We conducted a sequential exploratory mixed-methods study using three frameworks: TDF and COM-B for theoretical grounding, Context Mapping for accessible creative exploration, and Concept Mapping for quantitative structuring and validation. Five adapted stages mapped preconceptions of PA determinants among adolescents with mild ID from literature, experts (n=13), and teachers (n=8), and then adolescents' own perceptions (n=83-90) through: sensitizing (daily reflection postcards), generation (collage-based timelines), structuring (visual rating cards on a 7-point importance scale), and validation (a gamified quiz confirming the researchers' interpretations and highlighting differences between adolescents' perceptions and preconceptions from literature, experts, and teachers). Accessible participatory methods were co-designed with schools for the adolescents. Qualitative data from all sources were thematically analyzed to identify PA determinants and were mapped to TDF domains and COM-B components; quantitative data from adolescents' ratings of these determinants and validation quiz responses were analyzed using descriptive statistics, Mann-Whitney U tests, and hierarchical clustering to reveal consensus and individual variation.

**Results:** Twenty-nine PA determinants were identified and mapped to COM-B components: Opportunity (n=15), Motivation (n=8), and Capability (n=7). Adolescents emphasized emotional and social facilitators (e.g., fun activities, enjoyment, and peer or family support), while experts and teachers focused on capability barriers (e.g., impaired skills, cognitive fatigue). Quantitative ratings showed a positive bias toward facilitators (mean=5,09/7), with significant gender differences (P=.003), no age effect and weak within-group agreement (rwg<0.7), indicating variation in individual perceptions. Determinants perceived as facilitators by the adolescents showed greater consensus (ρ = 0.74) than barriers. Validation confirmed these patterns and highlighted divergences from stakeholder preconceptions, notably adolescents' positive ratings of determinants often assumed as barriers.

**Conclusions:** This study provides a theoretically grounded foundation for tailoring evidence-based digital interventions to adolescents with mild ID in PrO schools. Findings support a dual intervention strategy: group-level approaches for universal facilitators (higher agreement) and personalized strategies for individualized barriers (lower agreement). Digital health interventions are ideally positioned to deliver scalable facilitators alongside adaptive personalization algorithms to address barriers.

**Keywords:** Physical activity; adolescents; intellectual disability; behavior determinants; participatory research; theoretical domains framework; COM-B; digital health interventions.

## Quantitative Analysis

Perceived impact ratings of each PA determinant by adolescents were descriptively analyzed in Python, with the code openly available. Mean ratings and standard deviations were calculated for each determinant overall and by demographic subgroup (male vs. female; age groups 12-14 vs. 15-17). Mann-Whitney U tests compared ratings between groups. Hierarchical cluster analysis using Euclidean distance and average linkage method identified determinant clusters based on mean ratings (from barriers to facilitators) and within-group agreement coefficients (from low to high consensus), revealing patterns in the importance of determinants as perceived by the adolescents that inform the adaptation of interventions. Quiz responses by adolescents were analyzed using frequency distributions and Fleiss' Kappa to assess within-group agreement on categorical responses.


## Requirements

Install dependencies using:

```bash
pip install -r requirements.txt
```

## Citation

If you use this code or findings in your research, please cite:

> [Citation will be added once the article is published]

## License

[License information to be added]

## Contact

For questions about this repository or the LIFTS project, please contact [contact information to be added].

