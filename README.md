# AL/ML YouTube Revenue Predictor App     preview ; https://al-ml-youtube-revenue-predictor-app-byt5zrkn2zmshuxxtv2aff.streamlit.app/

This repository contains an end-to-end **ML model + Streamlit web app** to predict **YouTube ad revenue** from video performance and channel attributes.

## Project journey (high level)

1. **Dataset exploration**
   - Started from `youtube_ad_revenue_dataset (2) copy.csv`.
   - Performed cleaning, missing-value checks, and feature inspection.
2. **Model building**
   - Engineered/selected features such as views, likes, comments, watch time, video length, subscribers, and encoded categorical variables (category/device/country).
   - Trained a regression model.
3. **Preprocessing**
   - Used a scaler (`scaler.pkl`) to normalize numeric inputs.
4. **Packaging for deployment**
   - Serialized the trained model (`model.pkl`) and scaler for reuse in production.
5. **Streamlit deployment**
   - Built `app.py` to accept user inputs and run the prediction in the browser.

## Live app (local)

  https://youtube-adrevenuepredictor-51f814.netlify.app/   this was  the vision 

```bash
streamlit run app.py --server.address=0.0.0.0 --server.port=8501
```

My actual project from scratch .
https://al-ml-youtube-revenue-predictor-app-byt5zrkn2zmshuxxtv2aff.streamlit.app/

## What’s in this repo?

- `app.py` - Streamlit UI + inference logic
- `model.pkl` - trained ML model
- `scaler.pkl` - preprocessing scaler
- `youtube_ad_revenue_dataset (2) copy.csv` - source dataset
- `youtube_ad_revenue_analysis.ipynb` - exploratory analysis notebook

## How to contribute

- Improve feature engineering
- Experiment with different models/metrics
- Add better input validation + UI explanations

## Notes

- The app expects encoded values for categorical features (Category/Device/Country). These must match the encoding used during training.

