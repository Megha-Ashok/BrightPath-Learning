<h1 align="center"><b>BrightPath-Learning</b></h1>

## Project Overview & Motivation.
In today’s education system, academic progress is often measured only after exams, by which time it's too late for timely intervention. My intuition behind this project was to predict student performance early using various personal and academic features like gender, parental education, lunch type, and test preparation course. This enables proactive support instead of reactive judgment. The specialty of this project lies in its data-driven insight, built using multiple machine learning models and finalized with Linear Regression based on performance metrics. From a societal perspective, this system can be immensely helpful in identifying at-risk students early, providing them with targeted learning resources, and involving parents and teachers for necessary support. It bridges the gap between data and decisions in education, ensuring no student is left behind due to unnoticed academic struggles. In the current scenario — especially post-pandemic, where many students have learning gaps — such a solution becomes even more relevant and impactful

---

## Objective
Ultimately, this project strives to enable personalized learning interventions that improve student outcomes, reduce educational disparities, and foster data-driven decision-making within the education ecosystem.

---

## Target Users

This application is designed for multiple stakeholders including school educators, counselors, education researchers, and parents who want to gain insights into student performance and intervene proactively. It can also be valuable to educational policy makers aiming to understand broad factors affecting student achievement.

---

## Technologies & Architecture

The web application is built using Flask as the backend framework with Python handling the machine learning tasks. The front end uses HTML, CSS, and JavaScript to provide an interactive user interface where users can input student data and receive predictions in real-time. The machine learning models are trained using popular Python libraries such as scikit-learn and XGBoost. Model artifacts are saved as pickle files to enable smooth integration with the web app.

To ensure reliability and repeatability, I implemented MLOps practices including training and evaluation logging, artifact management, and model versioning. This setup ensures that any future updates or retraining efforts can be tracked and rolled out systematically.

---

## Features & Modules

### 1. Input Features

The model uses the following features as inputs:

- **Gender:** Male or Female.
- **Race/Ethnicity:** Group classification to capture demographic diversity.
- **Parental Level of Education:** Highest education attained by the student's parents.
- **Lunch Type:** Standard or free/reduced lunch, indicating socio-economic status.
- **Test Preparation Course:** Whether the student completed a test preparation course.

These features were chosen because they have a significant impact on academic performance, reflecting both environmental and educational preparation factors.

### 2. Output

The system predicts three continuous scores:

- Math Score
- Reading Score
- Writing Score

These predictions help in assessing student performance in core academic areas.

### 3. Model Selection & Evaluation

To build the best prediction model, I experimented with a wide range of regression algorithms:

- Linear Regression    
- Ridge Regression
- Lasso Regression
- K-Nearest Neighbors (KNN)
- Decision Tree Regressor
- Random Forest Regressor
- AdaBoost Regressor
- XGBoost Regressor

Each model was evaluated using metrics such as Mean Squared Error (MSE), Mean Absolute Error (MAE), and R² Score through cross-validation to ensure robust comparison. Despite several complex models tested, **Linear Regression emerged as the best balance of interpretability and accuracy**, achieving approximately 88% accuracy on the test data. This result confirms that simpler models can often capture underlying relationships well while maintaining transparency, which is crucial for educational applications.

### 5. MLOps Integration

The project includes a robust MLOps pipeline:

- Training metrics and model evaluation results are systematically logged for transparency.
- Model artifacts are stored as `.pkl` files, enabling version control and easy deployment.
- This approach supports continuous model improvement and safe rollout of updates.

---

## How to Use

Users input student information via the web interface. Upon submission, the app returns predicted scores for math, reading, and writing instantly. These predictions can highlight students who might require additional attention or support.

---

## Future Improvements

Building upon the current system, the following enhancements are planned to increase its educational impact:

- **Teacher Recommendation System:** Suggest personalized teachers or tutors for students based on predicted weaknesses and learning styles.
- **Student Learning Profile:** Track the grasping power of individual students and adapt teaching strategies accordingly.
- **Personalized Learning Paths:** Provide customized study plans and resources based on predicted performance.
- **Visual Progress Dashboards:** Enable educators and students to monitor academic growth over time through graphs and analytics.
- **Behavioral and Attendance Data Integration:** Incorporate more features to create a holistic student performance prediction.
- **Multilingual and Voice-Assisted Interfaces:** Enhance accessibility for diverse learners.
- **Real-Time Feedback and Model Retraining:** Allow the system to learn continuously from new student data to improve accuracy.

---

## Societal Impact

This project addresses critical gaps in education by enabling early identification of struggling students and facilitating personalized interventions. It supports educators in making data-driven decisions, helping reduce dropout rates and improve academic equity. By making performance prediction transparent and accessible, it helps bridge the educational divide and promotes student success in diverse communities.

---

## Technologies Used

- Python, Flask
- scikit-learn, XGBoost
- HTML, CSS, JavaScript
- MLOps tools for logging and artifact management
- Git for version control

---

## Conclusion

This project combines data science, machine learning, and software engineering to deliver a practical solution with real-world educational benefits. By predicting student performance and suggesting targeted support, it empowers educators and learners alike to achieve better academic outcomes.

---

