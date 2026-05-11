import pandas as pd
from prophet import Prophet


def run_forecast(df: pd.DataFrame, periods: int) -> pd.DataFrame:
    """Инициализация модели и получение прогноза."""
    model = Prophet(daily_seasonality=True)
    model.fit(df)

    future = model.make_future_dataframe(periods=periods)
    forecast = model.predict(future)

    # Возвращаем только прогнозную часть (последние 'periods' строк)
    return forecast.tail(periods)
