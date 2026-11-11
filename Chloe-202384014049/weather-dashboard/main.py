from geocode import get_coordinate
from weather_api import fetch_weather
from storage import save_weather_cache, load_weather_cache
from plot import plot_temp

def main():
    print("==== Weather Dashboard ====")
    city = input("请输入城市名：")
    lat, lon = get_coordinate(city)
    if lat is None:
        print("找不到该城市！")
        return

    print(f"获取坐标：lat={lat:.2f}, lon={lon:.2f}")
    weather = fetch_weather(lat, lon)
    save_weather_cache(weather)
    print("天气数据已缓存")

    plot_temp(weather)
    print("图表绘制完成！去assets文件夹查看图片")

    # 简单打印当日信息
    daily = weather["daily"]
    print("\n=== 7天预报概览 ===")
    for date, tmax, tmin in zip(daily["time"], daily["temperature_2m_max"], daily["temperature_2m_min"]):
        print(f"{date} | {tmin} ~ {tmax} ℃")


if __name__ == "__main__":
    main()