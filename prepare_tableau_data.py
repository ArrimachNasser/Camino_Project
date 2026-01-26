import pandas as pd
import os

# Paths
data_path = r"C:\Users\quint\Desktop\IronHack\WEEKS\FINALPROJ\data"
routes_path = os.path.join(data_path, "df_routes.csv")
trans_path = os.path.join(data_path, "df_trans.csv")

# 1. Geographic Mapping (Coordinates)
geo_data = {
    'Route': [
        'French Way', 'Via de la Plata', 'Primitive Way', 
        'Portuguese Way', 'Northern Way', 'English Way', 
        'Other Ways', 'Muxia-Finisterre'
    ],
    'Start_City': ['Roncesvalles', 'Seville', 'Oviedo', 'Lisbon', 'Irun', 'Ferrol', 'Other', 'Finisterre'],
    'Start_Lat': [43.016, 37.389, 43.361, 38.722, 43.339, 43.483, 42.000, 42.909],
    'Start_Long': [-1.233, -5.984, -5.850, -9.139, -1.789, -8.233, -4.000, -9.261],
    'End_City': ['Santiago', 'Santiago', 'Santiago', 'Santiago', 'Santiago', 'Santiago', 'Santiago', 'Santiago'],
    'End_Lat': [42.880, 42.880, 42.880, 42.880, 42.880, 42.880, 42.880, 42.880],
    'End_Long': [-8.546, -8.546, -8.546, -8.546, -8.546, -8.546, -8.546, -8.546]
}
df_geo = pd.DataFrame(geo_data)

# 2. Process Routes
df_routes = pd.read_csv(routes_path)
# Pivot routes to long format
df_routes_long = df_routes.melt(
    id_vars=['ID', 'Year', 'Month', 'Total'], 
    var_name='Route', 
    value_name='Count'
)
# Filter out 'Total' column from Route names if it ended up there
df_routes_long = df_routes_long[df_routes_long['Route'] != 'Total']

# Merge with geo coordinates
df_final_map = df_routes_long.merge(df_geo, on='Route', how='left')
df_final_map.to_csv(os.path.join(data_path, "df_routes_tableau_map.csv"), index=False)

# 3. Process Transportation (for side panel)
df_trans = pd.read_csv(trans_path)
df_trans_pivoted = df_trans.melt(
    id_vars=['ID', 'Year', 'Month', 'Total'],
    value_vars=['Foot', 'Bicycle', 'Other trans'],
    var_name='Travel_Method',
    value_name='Count'
)
df_trans_pivoted.to_csv(os.path.join(data_path, "df_trans_tableau_side.csv"), index=False)

print("Files created: df_routes_tableau_map.csv and df_trans_tableau_side.csv")
