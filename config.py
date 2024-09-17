from src.FileConfig import Config, Files

CONFIG: Config = [
    # Add your file paths here.
    Files(
        client="akasa-id", # 600
        dashboard="202408/DB/akasa-id.csv",
        console="202408/console/akasa-id.csv",
        output="202408/merge/akasa-id(1).csv",
    ),

]