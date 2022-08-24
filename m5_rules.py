import pandas as pd


def m5_rules(instance: pd.Series):
	hour = instance.get('Hour', 0)
	starting_minute = instance.get('Starting minute (inclussive)', 0)
	ending_minute = instance.get('Ending minute (exclussive)', 0)
	generated_power = instance.get('Generated power', 0)
	temperature_c = instance.get('TemperatureC', 0)
	dewpoint_c = instance.get('DewpointC', 0)
	pressure_hpa = instance.get('PressurehPa', 0)
	wind_direction_degrees = instance.get('WindDirectionDegrees', 0)
	wind_speed_kmh = instance.get('WindSpeedKMH', 0)
	wind_speed_gust_kmh = instance.get('WindSpeedGustKMH', 0)
	humidity = instance.get('Humidity', 0)
	hourly_precip_mm = instance.get('HourlyPrecipMM', 0)
	dailyrain_mm = instance.get('dailyrainMM', 0)
	solar_radiation_watts_m2 = instance.get('SolarRadiationWatts_m2', 0)

	# rule #1
	if hour <= 6.5: 
		generated_power = -0.0018 * hour - 0.0087 * temperature_c + 0.0382 * dewpoint_c - 0.0013 * pressure_hpa - 0.0004 * wind_direction_degrees - 0.0032 * wind_speed_kmh + 0.0029 * humidity + 0.0078 * dailyrain_mm + 0.0068 * solar_radiation_watts_m2 + 1.5143

	# rule #2
	elif hour > 19.5:
		generated_power = -0.0308 * hour + 0.0137 * temperature_c + 0.0769 * dewpoint_c - 0.0038 * pressure_hpa - 0.0003 * wind_direction_degrees - 0.0074 * wind_speed_kmh - 0.0048 * wind_speed_gust_kmh + 0.0092 * humidity + 0.0194 * dailyrain_mm + 0.0117 * solar_radiation_watts_m2 + 4.4667

	# rule #3 -> removed solar_radiation_watts_m2 <= 453 and solar_radiation_watts_m2 <= 92
	elif hour > 15.5 and pressure_hpa > 1015.5 and solar_radiation_watts_m2 <= 2.5:
		generated_power = -0.3721 * hour - 0.0071 * starting_minute - 0.0731 * temperature_c + 0.378 * dewpoint_c - 0.0224 * pressure_hpa - 0.0004 * wind_direction_degrees + 0.0075 * wind_speed_kmh + 0.021 * wind_speed_gust_kmh - 0.003 * humidity - 0.0698 * hourly_precip_mm + 0.0505 * dailyrain_mm + 0.0807 * solar_radiation_watts_m2 + 28.667

	# rule #4 -> removed solar_radiation_watts_m2 <= 461.5 and hour <= 8.5
	elif solar_radiation_watts_m2 <= 57 and hour <= 7.5:
		generated_power = 1.287 * hour + 0.0187 * starting_minute + 0.0373 * temperature_c + 0.4846 * dewpoint_c - 0.0152 * pressure_hpa + 0.001 * wind_direction_degrees - 0.0163 * wind_speed_kmh + 0.0117 * wind_speed_gust_kmh + 0.018 * humidity - 0.1395 * hourly_precip_mm + 0.0425 * dailyrain_mm + 4.3385 * solar_radiation_watts_m2 + 18.9759

	# rule #5 -> removed hour <= 14.5
	elif solar_radiation_watts_m2 <= 474 and hour <= 9.5 and hour > 8.5:
		generated_power = 2.3038 * hour + 6.0749 * starting_minute + 34.566 * temperature_c + 29.0293 * dewpoint_c - 1.6268 * pressure_hpa + 0.2184 * wind_direction_degrees - 0.0279 * wind_speed_kmh - 3.1794 * wind_speed_gust_kmh + 6.789 * humidity - 0.3227 * hourly_precip_mm + 0.0371 * dailyrain_mm + 1.2865 * solar_radiation_watts_m2 + 680.2044

	# rule #6 -> removed solar_radiation_watts_m2 <= 474 and solar_radiation_watts_m2 <= 143
	elif hour > 14.5 and humidity > 31.5 and solar_radiation_watts_m2 <= 41:
		generated_power = -1.3119 * hour - 0.0306 * starting_minute - 0.1573 * temperature_c + 0.8665 * dewpoint_c - 0.0705 * pressure_hpa + 0.0008 * wind_direction_degrees + 0.0042 * wind_speed_kmh + 0.0359 * wind_speed_gust_kmh - 0.0141 * humidity - 0.4223 * hourly_precip_mm + 0.0856 * dailyrain_mm + 5.3144 * solar_radiation_watts_m2 + 95.4264

	# rule #7 -> removed solar_radiation_watts_m2 <= 503.5
	elif hour > 14.5 and solar_radiation_watts_m2 <= 180:
		generated_power = -110.9766 * hour - 3.0917 * starting_minute - 33.1424 * temperature_c + 76.7131 * dewpoint_c - 0.0212 * pressure_hpa + 0.0004 * wind_direction_degrees + 0.009 * wind_speed_kmh + 3.7666 * wind_speed_gust_kmh - 9.6891 * humidity - 0.0769 * hourly_precip_mm + 10.1542 * dailyrain_mm + 2.7267 * solar_radiation_watts_m2 + 2550.5552

	# rule #8
	elif solar_radiation_watts_m2 <= 503.5 and hour > 8.5:
		generated_power = -68.7218 * hour - 0.0039 * starting_minute - 31.8507 * temperature_c + 120.8596 * dewpoint_c - 3.1682 * pressure_hpa + 0.2336 * wind_direction_degrees - 0.0043 * wind_speed_kmh + 11.0541 * wind_speed_gust_kmh - 2.6016 * humidity - 32.1475 * hourly_precip_mm + 18.661 * dailyrain_mm + 4.0083 * solar_radiation_watts_m2 + 3531.2595

	# rule #9 -> removed solar_radiation_watts_m2 > 461 and solar_radiation_watts_m2 > 641
	elif hour <= 13.5 and solar_radiation_watts_m2 > 771:
		generated_power = 91.0598 * hour - 4.3442 * starting_minute - 20.3612 * temperature_c + 69.8677 * dewpoint_c - 14.3905 * pressure_hpa + 0.0006 * wind_direction_degrees - 9.4262 * wind_speed_kmh + 8.0494 * wind_speed_gust_kmh - 4.3512 * humidity + 0.1353 * dailyrain_mm - 1.5138 * solar_radiation_watts_m2 + 19865.9997

	# rule #10 -> removed solar_radiation_watts_m2 > 461 and hour <= 14.5
	elif solar_radiation_watts_m2 <= 672 and solar_radiation_watts_m2 > 584.5 and hour <= 13.5:
		generated_power = -17.8358 * hour - 3.6405 * starting_minute - 69.7195 * temperature_c + 24.9418 * dewpoint_c + 20.9566 * pressure_hpa - 0.2902 * wind_speed_kmh + 5.7789 * wind_speed_gust_kmh - 13.9305 * humidity - 48.8352 * dailyrain_mm + 10.5527 * solar_radiation_watts_m2 - 22362.4322

	# rule #11 -> removed solar_radiation_watts_m2 <= 461
	elif solar_radiation_watts_m2 <= 80 and wind_speed_kmh > 0.5 and solar_radiation_watts_m2 > 27:
		generated_power = -1.9712 * hour - 1.1398 * starting_minute + 20.3172 * temperature_c - 5.3767 * dewpoint_c - 2.959 * pressure_hpa - 0.0013 * wind_direction_degrees - 0.1216 * wind_speed_kmh - 0.2033 * wind_speed_gust_kmh + 5.0457 * humidity + 0.1372 * dailyrain_mm + 3.1813 * solar_radiation_watts_m2 + 2548.6047

	# rule #12 -> removed solar_radiation_watts_m2 <= 461
	elif solar_radiation_watts_m2 <= 56.5 and wind_speed_kmh > 0.5:
		generated_power = -1.7867 * hour + 0.0632 * starting_minute - 0.2793 * temperature_c + 0.3003 * dewpoint_c - 0.0231 * pressure_hpa - 0.193 * wind_speed_kmh - 0.2457 * wind_speed_gust_kmh + 0.0805 * humidity - 0.069 * dailyrain_mm + 0.1721 * solar_radiation_watts_m2 + 89.2979

	# rule #13
	elif solar_radiation_watts_m2 <= 461 and dewpoint_c <= 6.5 and pressure_hpa > 1024.5:
		generated_power = -1.6037 * hour + 0.0125 * starting_minute - 1.5367 * temperature_c + 3.3484 * dewpoint_c + 0.0077 * pressure_hpa - 0.1859 * wind_speed_kmh - 0.2872 * wind_speed_gust_kmh - 0.3937 * humidity + 0.1837 * dailyrain_mm + 0.1544 * solar_radiation_watts_m2 + 242.6296

	# rule #14
	elif solar_radiation_watts_m2 <= 461 and dewpoint_c <= 6.5:
		generated_power = 0.2336 * hour + 1.6042 * starting_minute - 17.4556 * temperature_c + 23.8533 * dewpoint_c - 0.0082 * pressure_hpa - 0.0126 * wind_direction_degrees - 0.2156 * wind_speed_kmh - 0.3476 * wind_speed_gust_kmh - 0.1157 * humidity + 0.7689 * solar_radiation_watts_m2 + 253.7664

	# rule #15 -> removed solar_radiation_watts_m2 > 672 and hour <= 14.5
	elif hour <= 13.5 and solar_radiation_watts_m2 > 725 and pressure_hpa > 1019.5:
		generated_power = -106.5762 * hour - 3.2543 * starting_minute - 94.3804 * temperature_c + 56.8714 * dewpoint_c - 16.6416 * pressure_hpa - 0.504 * wind_direction_degrees - 0.3098 * wind_speed_kmh + 0.0703 * wind_speed_gust_kmh - 23.5297 * humidity + 0.313 * dailyrain_mm + 0.9768 * solar_radiation_watts_m2 + 24956.4898

	# rule #16 -> removed hour <= 14.5
	elif solar_radiation_watts_m2 > 672 and hour <= 13.5 and humidity > 66.5:
		generated_power = 178.5439 * hour - 4.5153 * starting_minute - 9.2807 * temperature_c + 6.4045 * dewpoint_c + 3.7888 * pressure_hpa - 0.0427 * wind_direction_degrees - 15.9364 * wind_speed_kmh - 8.635 * wind_speed_gust_kmh - 2.8643 * humidity + 0.3629 * dailyrain_mm + 8.9496 * solar_radiation_watts_m2 - 7446.007

	# rule #17 -> removed solar_radiation_watts_m2 > 461 and hour <= 14.5
	elif solar_radiation_watts_m2 <= 672 and hour <= 13.5 and solar_radiation_watts_m2 > 560 and humidity <= 58.5:
		generated_power = -2.51 * hour - 4.1125 * starting_minute + 3.6113 * temperature_c + 18.7524 * dewpoint_c + 8.0947 * pressure_hpa - 0.0247 * wind_direction_degrees - 1.1337 * wind_speed_kmh - 0.369 * wind_speed_gust_kmh - 4.7442 * humidity + 2.1245 * dailyrain_mm + 0.4888 * solar_radiation_watts_m2 - 5311.6518

	# rule #18 -> removed hour > 14.5
	elif solar_radiation_watts_m2 <= 672 and solar_radiation_watts_m2 > 461 and pressure_hpa <= 1020.5 and humidity > 51 and hour > 15.5:
		generated_power = -60.1802 * hour - 6.3373 * starting_minute + 143.1076 * temperature_c - 123.3497 * dewpoint_c - 12.7259 * pressure_hpa - 0.1988 * wind_direction_degrees - 1.5357 * wind_speed_kmh - 21.2309 * wind_speed_gust_kmh + 29.9795 * humidity + 17.3782 * dailyrain_mm - 0.7407 * solar_radiation_watts_m2 + 13211.4487

	# rule #19 -> removed hour <= 14.5
	elif solar_radiation_watts_m2 <= 672 and solar_radiation_watts_m2 > 461 and hour <= 13.5 and pressure_hpa <= 1019.5 and hour > 9.5:
		generated_power = 198.5546 * hour - 0.8605 * starting_minute - 0.8504 * temperature_c + 0.9764 * dewpoint_c + 1.8655 * pressure_hpa - 0.0296 * wind_direction_degrees - 3.8376 * wind_speed_kmh - 13.5167 * wind_speed_gust_kmh - 1.3305 * humidity + 4.8194 * dailyrain_mm + 1.7086 * solar_radiation_watts_m2 - 1770.1459

	# rule #20 -> removed hour <= 14.5
	elif solar_radiation_watts_m2 <= 672 and solar_radiation_watts_m2 > 461 and hour <= 13.5 and hour > 12.5:
		generated_power = -5.9587 * hour - 0.9309 * starting_minute + 9.9568 * temperature_c + 14.7026 * dewpoint_c + 4.8533 * pressure_hpa - 0.0302 * wind_direction_degrees - 0.6433 * wind_speed_kmh - 0.4504 * wind_speed_gust_kmh - 3.6956 * humidity + 20.3926 * dailyrain_mm + 4.5307 * solar_radiation_watts_m2 - 4395.065

	# rule #21 -> removed solar_radiation_watts_m2 <= 672 and hour <= 14.5 hour > 9.5
	elif solar_radiation_watts_m2 > 461 and hour <= 13 and solar_radiation_watts_m2 <= 549 and dewpoint_c <= 7.5 and hour > 10.5:
		generated_power = 233.1603 * hour + 0.0722 * starting_minute - 6.9391 * temperature_c + 52.9981 * dewpoint_c + 6.9839 * pressure_hpa - 0.5285 * wind_direction_degrees - 0.3866 * wind_speed_kmh - 0.4344 * wind_speed_gust_kmh - 4.3976 * humidity + 3.4246 * dailyrain_mm + 7.3788 * solar_radiation_watts_m2 - 11040.1317

	# rule #22 -> removed hour <= 14.5
	elif solar_radiation_watts_m2 > 505 and solar_radiation_watts_m2 <= 672 and hour <= 13 and hour > 9.5:
		generated_power = -18.0806 * hour - 6.6297 * starting_minute - 30.6282 * temperature_c + 60.4302 * dewpoint_c + 23.937 * pressure_hpa + 0.3751 * wind_direction_degrees - 10.1369 * wind_speed_kmh - 0.0556 * wind_speed_gust_kmh - 14.2454 * humidity + 1.4498 * dailyrain_mm + 7.8858 * solar_radiation_watts_m2 - 24634.2237

	# rule #23 -> removed solar_radiation_watts_m2 <= 672
	elif solar_radiation_watts_m2 > 461 and hour <= 14.5 and starting_minute > 22.5 and solar_radiation_watts_m2 <= 570.5:
		generated_power = -28.9256 * hour - 3.6675 * starting_minute - 59.5114 * temperature_c - 22.6454 * dewpoint_c + 1.3737 * pressure_hpa - 1.991 * wind_direction_degrees - 0.2877 * wind_speed_kmh - 0.7023 * wind_speed_gust_kmh - 6.7226 * humidity + 5.7275 * dailyrain_mm + 0.0377 * solar_radiation_watts_m2 + 3246.7275

	# rule #24
	elif solar_radiation_watts_m2 <= 672 and hour > 9 and hour <= 14.5:
		generated_power = -42.8873 * hour - 35.3838 * starting_minute - 72.0264 * temperature_c + 130.2409 * dewpoint_c - 20.3714 * pressure_hpa - 0.0794 * wind_direction_degrees - 0.4092 * wind_speed_kmh - 1.0028 * wind_speed_gust_kmh - 19.8797 * humidity + 5.7254 * dailyrain_mm + 0.437 * solar_radiation_watts_m2 + 25710.6992

	# rule #25 -> removed solar_radiation_watts_m2 > 672
	elif hour > 14.5 and solar_radiation_watts_m2 > 772.5 and dewpoint_c <= 11.5:
		generated_power = -663.1051 * hour - 13.3685 * starting_minute - 39.4337 * temperature_c + 6.1689 * dewpoint_c - 10.971 * pressure_hpa + 0.0468 * wind_direction_degrees + 0.5227 * wind_speed_kmh - 23.7302 * wind_speed_gust_kmh - 14.0748 * humidity + 1.9529 * solar_radiation_watts_m2 + 24425.499

	# rule #26
	elif solar_radiation_watts_m2 <= 672 and solar_radiation_watts_m2 > 299 and pressure_hpa > 1020.5 and humidity <= 58.5:
		generated_power = -13.0167 * hour - 4.9074 * starting_minute - 1.0893 * temperature_c + 4.0353 * dewpoint_c - 2.4601 * pressure_hpa - 0.0007 * wind_direction_degrees - 0.0969 * wind_speed_kmh + 0.8886 * wind_speed_gust_kmh + 1.6072 * humidity + 14.6193 * dailyrain_mm + 0.7928 * solar_radiation_watts_m2 + 3042.7499

	# rule #27 -> removed solar_radiation_watts_m2 <= 672
	elif solar_radiation_watts_m2 > 299 and solar_radiation_watts_m2 <= 614 and dewpoint_c > 8.5 and pressure_hpa > 1019.5:
		generated_power = -11.6684 * hour - 0.1878 * starting_minute - 0.9568 * temperature_c + 15.9562 * dewpoint_c - 9.5098 * pressure_hpa - 0.2408 * wind_direction_degrees - 0.2748 * wind_speed_kmh + 9.0944 * wind_speed_gust_kmh + 1.3729 * humidity + 0.5721 * dailyrain_mm + 1.012 * solar_radiation_watts_m2 + 9968.3019

	# rule #28 -> removed solar_radiation_watts_m2 <= 672
	elif solar_radiation_watts_m2 <= 299 and solar_radiation_watts_m2 > 106 and humidity <= 91.5 and humidity > 60.5 and pressure_hpa <= 1025.5 and dewpoint_c <= 8.5 and wind_speed_gust_kmh <= 15:
		generated_power = 22.9257 * hour + 0.594 * starting_minute + 3.5213 * temperature_c + 22.8086 * dewpoint_c + 0.1138 * pressure_hpa + 0.0625 * wind_direction_degrees - 0.6728 * wind_speed_kmh + 5.0434 * wind_speed_gust_kmh + 0.5098 * humidity + 0.6157 * dailyrain_mm + 0.2601 * solar_radiation_watts_m2 - 260.0738

	# rule #29
	elif solar_radiation_watts_m2 <= 672 and solar_radiation_watts_m2 > 301.5 and dewpoint_c <= 8.5:
		generated_power = -9.0436 * hour - 4.0231 * starting_minute + 25.574 * temperature_c + 16.194 * dewpoint_c - 24.8472 * pressure_hpa - 0.6852 * wind_direction_degrees + 7.8372 * wind_speed_kmh + 10.864 * wind_speed_gust_kmh + 19.8207 * humidity + 2.3782 * dailyrain_mm + 2.0941 * solar_radiation_watts_m2 + 23736.875

	# rule #30
	elif hour <= 9 and solar_radiation_watts_m2 > 106 and humidity <= 92.5:
		generated_power = 243.0064 * hour + 3.7496 * starting_minute + 29.2339 * temperature_c - 54.6061 * dewpoint_c + 0.1547 * pressure_hpa - 0.0331 * wind_direction_degrees - 6.7059 * wind_speed_kmh - 0.221 * wind_speed_gust_kmh + 3.57 * humidity + 0.6592 * dailyrain_mm + 0.3194 * solar_radiation_watts_m2 - 1776.7175

	# rule #31 -> removed hour <= 14.5
	elif solar_radiation_watts_m2 > 671.5 and hour <= 13.5 and pressure_hpa > 1025.5 and starting_minute <= 42.5:
		generated_power = -228.1836 * hour - 4.5157 * starting_minute + 0.7803 * temperature_c - 10.1331 * dewpoint_c + 5.4299 * pressure_hpa - 0.018 * wind_direction_degrees + 6.285 * wind_speed_gust_kmh + 0.6391 * humidity + 0.2603 * dailyrain_mm + 6.8402 * solar_radiation_watts_m2 - 2994.8094

	# rule #32 -> removed hour <= 14.5 and hour <= 13.5
	elif solar_radiation_watts_m2 > 671.5 and solar_radiation_watts_m2 <= 737.5 and hour <= 12.5 and dewpoint_c <= 7.5:
		generated_power = -183.5307 * hour - 1.8117 * starting_minute - 11.6209 * temperature_c - 18.4494 * dewpoint_c + 26.6505 * pressure_hpa + 0.0416 * wind_direction_degrees - 0.3146 * wind_speed_kmh + 6.5627 * wind_speed_gust_kmh - 10.9326 * humidity + 0.2009 * dailyrain_mm + 8.0293 * solar_radiation_watts_m2 - 25486.4292

	# rule #33 -> removed solar_radiation_watts_m2 > 671.5
	elif hour <= 14.5 and solar_radiation_watts_m2 > 706 and starting_minute > 37.5 and hour > 12.5:
		generated_power = -840.599 * hour - 38.0295 * starting_minute - 41.7635 * temperature_c + 51.2193 * dewpoint_c - 13.8382 * pressure_hpa - 0.302 * wind_speed_kmh - 0.7486 * wind_speed_gust_kmh - 9.0477 * humidity + 3.9384 * solar_radiation_watts_m2 + 28725.366

	# rule #34 -> removed hour <= 14.5
	elif solar_radiation_watts_m2 > 671.5 and solar_radiation_watts_m2 <= 714.5 and hour <= 13.5:
		generated_power = -167.9328 * hour - 5.1073 * starting_minute - 5.0873 * temperature_c + 31.0622 * dewpoint_c + 35.0567 * pressure_hpa - 0.1775 * wind_direction_degrees - 3.4093 * wind_speed_kmh + 0.7415 * wind_speed_gust_kmh + 0.9891 * humidity - 3.5513 * dailyrain_mm + 10.7255 * solar_radiation_watts_m2 - 37290.2885

	# rule #35 -> removed solar_radiation_watts_m2 > 509
	elif hour <= 14.5 and solar_radiation_watts_m2 > 716 and temperature_c > 16.5:
		generated_power = -161.6337 * hour - 4.863 * starting_minute + 48.2184 * temperature_c - 103.0895 * dewpoint_c - 1.3773 * pressure_hpa - 0.0426 * wind_direction_degrees - 7.8494 * wind_speed_kmh + 9.7625 * wind_speed_gust_kmh + 23.0701 * humidity - 5.3921 * dailyrain_mm + 3.1435 * solar_radiation_watts_m2 + 4316.9908

	# rule #36 -> removed hour > 9.5 and hour > 14.5
	elif hour > 15.5 and solar_radiation_watts_m2 <= 683:
		generated_power = -32.542 * hour - 5.9655 * starting_minute + 11.4334 * temperature_c + 10.5935 * dewpoint_c - 0.3497 * pressure_hpa + 1.1136 * wind_speed_kmh + 1.1667 * wind_speed_gust_kmh - 2.1722 * humidity + 1.9047 * solar_radiation_watts_m2 + 907.5248

	# rule #37 -> removed hour > 9.5
	elif hour > 14.5:
		generated_power = -580.2943 * hour - 9.8887 * starting_minute - 72.0372 * temperature_c + 127.7521 * dewpoint_c - 7.6979 * pressure_hpa + 1.3907 * wind_speed_gust_kmh - 23.1422 * humidity + 20.0376 * dailyrain_mm + 2.1498 * solar_radiation_watts_m2 + 18897.9074

	# rule #38 -> removed solar_radiation_watts_m2 > 714.5
	elif hour > 9.5 and solar_radiation_watts_m2 > 794.5:
		generated_power = -13.3029 * starting_minute - 59.6173 * temperature_c + 62.6065 * dewpoint_c - 6.0373 * pressure_hpa - 2.6731 * wind_speed_kmh - 13.1259 * humidity - 36.7968 * dailyrain_mm + 1.7395 * solar_radiation_watts_m2 + 10838.9002

	# rule #39
	elif hour > 9.5 and solar_radiation_watts_m2 <= 714.5 and humidity <= 40.5:
		generated_power = -26.688 * starting_minute - 69.8859 * temperature_c + 103.7689 * dewpoint_c + 21.195 * pressure_hpa - 0.2597 * wind_direction_degrees - 4.8443 * wind_speed_gust_kmh - 17.7634 * humidity + 2.4237 * solar_radiation_watts_m2 - 18693.5361

	# rule #40
	elif hour <= 9.5 and solar_radiation_watts_m2 > 106 and pressure_hpa > 1021.5:
		generated_power = 116.4872 * hour + 0.615 * starting_minute + 43.9006 * temperature_c - 6.311 * dewpoint_c - 12.194 * pressure_hpa - 0.05 * wind_direction_degrees - 3.5327 * wind_speed_gust_kmh + 2.5367 * humidity + 418.8145 * dailyrain_mm + 0.419 * solar_radiation_watts_m2 + 11259.2999

	# rule #41
	else:
		generated_power = 110.6441 * temperature_c - 119.076 * dewpoint_c - 10.4939 * pressure_hpa - 10.9899 * wind_speed_gust_kmh + 23.9538 * humidity + 5.1262 * solar_radiation_watts_m2 + 8520.6151

	return generated_power
