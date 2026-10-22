#### md file created from:		https://markdownlivepreview.com/
<br>

# Final Course Project – Phase 1: Project Proposal

For the first phase of the course project, you are required to select a healthcare-related dataset from an online source and briefly describe the project you plan to work on.
<br>

---

***Your proposal should include:***

1.  Project Title: A short, descriptive title for your project.

        How Joint Bracing Restricts Lower-Limb Mobility Across Consecutive Strides

        Does Joint Bracing Hinder Natural Mobility or Force Better Stride Consistency?

2.  Project Overview: Briefly explain the purpose of your project and what you would like to investigate, analyze, or predict using the selected dataset.

    *Hypothesis: While wearing a brace will predictably hinder mobility by shrinking a person's overall range of motion, it will simultaneously help them by acting as a mechanical stabilizer, causing their consecutive strides to become significantly more uniform and consistent compared to walking unbraced.*

3.  Dataset Description: Identify the dataset, provide its source (including the URL), and briefly describe the information it contains.

4.  Planned Analysis: Briefly describe how you plan to explore and analyze the data using Python and the machine-learning methods covered in the course.

---

_Submission Requirements:_

* Maximum length: 1 page

* File format: Microsoft Word or PDF

* No Python code or completed analysis is required at this stage.

* This proposal will serve as the starting point for your final course project.

---
<br>

## Purpose of the Project:

The purpose of this project is to investigate how mechanical joint restrictions alter baseline human locomotion across a sample of healthy subjects. Because lower-limb braces are traditionally designed to restrict movement, this study aims to evaluate if these devices serve strictly as a hindrance, or if they simultaneously function as dynamic stabilizers that enforce movement regularity across the entire lower body.

<u>What the Project Investigates, Analyzes, and Predicts:</u>



* Investigates: The tension between physical restriction and stabilization across the lower kinetic chain. It explores how a restraint applied to a single location impacts overall walking harmony across multiple connected joints.

* Analyzes: The continuous joint angles (measured in degrees) across a series of complete, normalized stride cycles (0% to 100%). Specifically, the analysis tracks three distinct joints—the ankle, knee, and hip—bilaterally (on both the left and right legs). These measurements are evaluated under one of three conditions:
	1. Condition 1: Unbraced (Normal baseline walking)
	2. Condition 2: Knee brace applied to the right leg
	3. Condition 3: Ankle brace applied to the right leg

* Predicts/Tests: The core hypothesis that while a unilateral restriction will predictably reduce absolute mobility (Range of Motion) in the targeted joint, it will simultaneously act as a structural anchor that forces consecutive stride cycles to become highly uniform and consistent across all three joints.


---
<br>

## Dataset Description

The Multivariate Gait Data dataset is sourced from the UCI Machine Learning Repository at https://archive.ics.uci.edu/dataset/760/multivariate+gait+data.

Dataset Description

The dataset contains 181,800 instances and 7 features detailing the biomechanical analysis of human locomotion. It is a sequential, multivariate time-series dataset that captures continuous joint angles (measured in degrees) for the ankle, knee, and hip across both legs (bilateral).

Key Information Contained

• Subjects: Data collected from 10 healthy individuals.
• Conditions: 3 walking settings on a treadmill: normal (unbraced), knee braced (right knee), and ankle braced (right ankle).
• Replications: Each setting tracks 10 consecutive gait cycles starting and ending at heel-strike.
• Time Alignment: Each gait cycle is normalized into 101 time points representing 0% to 100% of the stride sequence.

---
<br>

## Planned Analysis:

To explore and analyze the dataset, the plan relies on a structured machine-learning pipeline utilizing Python and standard foundational algorithms.
The analysis is broken down into four key stages:

1. Exploratory Data Analysis (EDA)

    * Data Visualization: Plotting continuous joint angles across the 0% to 100% gait cycle using matplotlib to visually inspect differences between the three walking conditions.
    * Anomaly Detection: Inspecting the data structure for missing values, out-of-range degrees, or incomplete stride replications.

2. Feature Engineering & Dimensionality Reduction

    * Summary Statistic Extraction: Transforming raw, complex time-series sequences into simplified numeric features by calculating Maximum Angle, Minimum Angle, and Range of Motion (ROM) for each of the three joints (ankle, knee, hip).
    * Data Reshaping: Pivot-transforming the long gait cycle rows into a structured wide format where each individual stride replication represents a single sample observation.

3. Predictive Machine-Learning Modeling

    * Data Partitioning: Splitting the processed dataset into independent training (70%) and testing (30%) subsets using stratified sampling to maintain class balance.
    * Supervised Classification: Training a Random Forest Classifier or Decision Tree algorithm to predict the target label—the specific bracing condition (1, 2, or 3)—based on the extracted joint mobility features.

4. Model Evaluation & Performance Metrics

    * Accuracy Assessment: Generating a classification report to measure precision, recall, and F1-score for each condition type.
    * Feature Importance Analysis: Extracting model weightings to determine which specific joint angles (e.g., right knee vs. right hip) provide the strongest predictive power when detecting physical restrictions.



<br>
<br>
<br>











