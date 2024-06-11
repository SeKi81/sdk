// automatically generated by the FlatBuffers compiler, do not modify

package com.openmeteo.sdk

@Suppress("unused")
class Variable private constructor() {
    companion object {
        const val undefined: UByte = 0u
        const val apparent_temperature: UByte = 1u
        const val cape: UByte = 2u
        const val cloud_cover: UByte = 3u
        const val cloud_cover_high: UByte = 4u
        const val cloud_cover_low: UByte = 5u
        const val cloud_cover_mid: UByte = 6u
        const val daylight_duration: UByte = 7u
        const val dew_point: UByte = 8u
        const val diffuse_radiation: UByte = 9u
        const val diffuse_radiation_instant: UByte = 10u
        const val direct_normal_irradiance: UByte = 11u
        const val direct_normal_irradiance_instant: UByte = 12u
        const val direct_radiation: UByte = 13u
        const val direct_radiation_instant: UByte = 14u
        const val et0_fao_evapotranspiration: UByte = 15u
        const val evapotranspiration: UByte = 16u
        const val freezing_level_height: UByte = 17u
        const val growing_degree_days: UByte = 18u
        const val is_day: UByte = 19u
        const val latent_heat_flux: UByte = 20u
        const val leaf_wetness_probability: UByte = 21u
        const val lifted_index: UByte = 22u
        const val lightning_potential: UByte = 23u
        const val precipitation: UByte = 24u
        const val precipitation_hours: UByte = 25u
        const val precipitation_probability: UByte = 26u
        const val pressure_msl: UByte = 27u
        const val rain: UByte = 28u
        const val relative_humidity: UByte = 29u
        const val runoff: UByte = 30u
        const val sensible_heat_flux: UByte = 31u
        const val shortwave_radiation: UByte = 32u
        const val shortwave_radiation_instant: UByte = 33u
        const val showers: UByte = 34u
        const val snow_depth: UByte = 35u
        const val snow_height: UByte = 36u
        const val snowfall: UByte = 37u
        const val snowfall_height: UByte = 38u
        const val snowfall_water_equivalent: UByte = 39u
        const val sunrise: UByte = 40u
        const val sunset: UByte = 41u
        const val soil_moisture: UByte = 42u
        const val soil_moisture_index: UByte = 43u
        const val soil_temperature: UByte = 44u
        const val surface_pressure: UByte = 45u
        const val surface_temperature: UByte = 46u
        const val temperature: UByte = 47u
        const val terrestrial_radiation: UByte = 48u
        const val terrestrial_radiation_instant: UByte = 49u
        const val total_column_integrated_water_vapour: UByte = 50u
        const val updraft: UByte = 51u
        const val uv_index: UByte = 52u
        const val uv_index_clear_sky: UByte = 53u
        const val vapour_pressure_deficit: UByte = 54u
        const val visibility: UByte = 55u
        const val weather_code: UByte = 56u
        const val wind_direction: UByte = 57u
        const val wind_gusts: UByte = 58u
        const val wind_speed: UByte = 59u
        const val vertical_velocity: UByte = 60u
        const val geopotential_height: UByte = 61u
        const val wet_bulb_temperature: UByte = 62u
        const val river_discharge: UByte = 63u
        const val wave_height: UByte = 64u
        const val wave_period: UByte = 65u
        const val wave_direction: UByte = 66u
        const val wind_wave_height: UByte = 67u
        const val wind_wave_period: UByte = 68u
        const val wind_wave_peak_period: UByte = 69u
        const val wind_wave_direction: UByte = 70u
        const val swell_wave_height: UByte = 71u
        const val swell_wave_period: UByte = 72u
        const val swell_wave_peak_period: UByte = 73u
        const val swell_wave_direction: UByte = 74u
        const val pm10: UByte = 75u
        const val pm2p5: UByte = 76u
        const val dust: UByte = 77u
        const val aerosol_optical_depth: UByte = 78u
        const val carbon_monoxide: UByte = 79u
        const val nitrogen_dioxide: UByte = 80u
        const val ammonia: UByte = 81u
        const val ozone: UByte = 82u
        const val sulphur_dioxide: UByte = 83u
        const val alder_pollen: UByte = 84u
        const val birch_pollen: UByte = 85u
        const val grass_pollen: UByte = 86u
        const val mugwort_pollen: UByte = 87u
        const val olive_pollen: UByte = 88u
        const val ragweed_pollen: UByte = 89u
        const val european_aqi: UByte = 90u
        const val european_aqi_pm2p5: UByte = 91u
        const val european_aqi_pm10: UByte = 92u
        const val european_aqi_nitrogen_dioxide: UByte = 93u
        const val european_aqi_ozone: UByte = 94u
        const val european_aqi_sulphur_dioxide: UByte = 95u
        const val us_aqi: UByte = 96u
        const val us_aqi_pm2p5: UByte = 97u
        const val us_aqi_pm10: UByte = 98u
        const val us_aqi_nitrogen_dioxide: UByte = 99u
        const val us_aqi_ozone: UByte = 100u
        const val us_aqi_sulphur_dioxide: UByte = 101u
        const val us_aqi_carbon_monoxide: UByte = 102u
        const val sunshine_duration: UByte = 103u
        const val convective_inhibition: UByte = 104u
        const val shortwave_radiation_clear_sky: UByte = 105u
        const val global_tilted_irradiance: UByte = 106u
        const val global_tilted_irradiance_instant: UByte = 107u
        const val ocean_current_velocity: UByte = 108u
        const val ocean_current_direction: UByte = 109u
    }
}
