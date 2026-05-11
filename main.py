from fastapi import FastAPI, HTTPException
import uvicorn
from src.core.pydantic_models import PredictionPoint, PredictRequest, PredictResponse
from src.core.model import run_forecast
from src.core.data_load import fetch_data

app = FastAPI(title="Financial Prediction Service")


@app.post("/predict", response_model=PredictResponse)
async def predict(request: PredictRequest):
    try:
        df = fetch_data(request.ticker)

        forecast_df = run_forecast(df, request.days)

        response_data = []
        for _, row in forecast_df.iterrows():
            response_data.append(
                PredictionPoint(
                    date=row["ds"].date(),
                    value=round(row["yhat"], 4),
                    lower=round(row["yhat_lower"], 4),
                    upper=round(row["yhat_upper"], 4),
                )
            )

        return PredictResponse(ticker=request.ticker, forecast=response_data)

    except ValueError as ve:
        raise HTTPException(status_code=404, detail=str(ve))
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Prediction error: {str(e)}")


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
