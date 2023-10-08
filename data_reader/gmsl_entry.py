# class represents a 'global mean sea level' data entry

"""
HDR ====================
HDR
HDR Global Mean Sea Level (GMSL) variations from TPJAOS v5.1
HDR
HDR column description 
HDR 1 altimeter type 0=dual-frequency  999=single frequency (ie Poseidon-1) 
HDR 2 merged file cycle # 
HDR 3 year+fraction of year (mid-cycle) 
HDR 4 number of observations 
HDR 5 number of weighted observations 
HDR 6 GMSL (Global Isostatic Adjustment (GIA) not applied) variation (mm) with respect to 20-year TOPEX/Jason collinear mean reference 
HDR 7 standard deviation of GMSL (GIA not applied) variation estimate (mm)
HDR 8 smoothed (60-day Gaussian type filter) GMSL (GIA not applied) variation (mm)  
HDR 9 GMSL (Global Isostatic Adjustment (GIA) applied) variation (mm) with respect to 20-year TOPEX/Jason collinear mean reference 
HDR 10 standard deviation of GMSL (GIA applied) variation estimate (mm)
HDR 11 smoothed (60-day Gaussian type filter) GMSL (GIA applied) variation (mm)
HDR 12 smoothed (60-day Gaussian type filter) GMSL (GIA applied) variation (mm); annual and semi-annual signal removed
HDR 13 smoothed (60-day Gaussian type filter) GMSL (GIA not applied) variation (mm); annual and semi-annual signal removed
HDR
HDR Missing or bad value flag: 99900.000 
HDR 
HDR TOPEX/Jason 1996-2016 collinear mean reference derived from cycles 121 to 858. 
HDR 
HDR Header_End---------------------------------------
"""


class GMSLEntry:
    def __init__(
        self,
        altimeter_type: int,  # 0
        merged_file_cycle: int,  # 11
        year_fraction: float,  # 1993.0115260
        num_observations: int,  # 452600
        num_weighted_observations: float,  # 327401.31
        gmsl_variation: float,  # -38.61
        gmsl_variation_std: float,  # 89
        smoothed_gmsl_variation: float,  # -38.78
        gmsl_variation_gia: float,  # 89.88
        gmsl_variation_gia_std: float,
        smoothed_gmsl_variation_gia: float,
        smoothed_gmsl_variation_gia_annual_semi_annual_removed: float,
        smoothed_gmsl_variation_annual_semi_annual_removed: float
    ):
        self.altimeter_type = altimeter_type
        self.merged_file_cycle = merged_file_cycle
        self.year_fraction = year_fraction
        self.num_observations = num_observations
        self.num_weighted_observations = num_weighted_observations
        self.gmsl_variation = gmsl_variation
        self.gmsl_variation_std = gmsl_variation_std
        self.smoothed_gmsl_variation = smoothed_gmsl_variation
        self.gmsl_variation_gia = gmsl_variation_gia
        self.gmsl_variation_gia_std = gmsl_variation_gia_std
        self.smoothed_gmsl_variation_gia = smoothed_gmsl_variation_gia
        self.smoothed_gmsl_variation_gia_annual_semi_annual_removed = smoothed_gmsl_variation_gia_annual_semi_annual_removed
        self.smoothed_gmsl_variation_annual_semi_annual_removed = smoothed_gmsl_variation_annual_semi_annual_removed

    def get_tuple(self):
        return (
            self.altimeter_type,
            self.merged_file_cycle,
            self.year_fraction,
            self.num_observations,
            self.num_weighted_observations,
            self.gmsl_variation,
            self.gmsl_variation_std,
            self.smoothed_gmsl_variation,
            self.gmsl_variation_gia,
            self.gmsl_variation_gia_std,
            self.smoothed_gmsl_variation_gia,
            self.smoothed_gmsl_variation_gia_annual_semi_annual_removed,
            self.smoothed_gmsl_variation_annual_semi_annual_removed
        )
