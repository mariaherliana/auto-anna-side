from src.FileConfig import Config, Files

CONFIG: Config = [
    # Add your file paths here.
    Files(
        client="moladin-cs-id", # 600 (2131141038)
        dashboard="202409/DB/moladin-cs-id.csv",
        console="202409/console/moladin-cs-id.csv",
        output="202409/merge/moladin-cs-id.csv",
    ),
    Files(
        client="moladin-riskandcompliance-id", # 600 (2131141039)
        dashboard="202409/DB/moladin-riskandcompliance-id.csv",
        console="202409/console/moladin-riskandcompliance-id.csv",
        output="202409/merge/moladin-riskandcompliance-id.csv",
    ),
    Files(
        client="moladin-sales-id", # 600 (85592164055, 88978012571)
        dashboard="202409/DB/moladin-sales-id.csv",
        console="202409/console/moladin-sales-id.csv",
        output="202409/merge/moladin-sales-id.csv",
    ),
    Files(
        client="dipomitsubishi-id", # 800 
        dashboard="202409/DB/dipomitsubishi-id.csv",
        console="202409/console/dipomitsubishi-id.csv",
        output="202409/merge/dipomitsubishi-id.csv",
    ),
    Files(
        client="akasa-id", # 900 (81197800082)
        dashboard="202409/DB/akasa-id.csv",
        console="202409/console/akasa-id.csv",
        output="202409/merge/akasa-id.csv",
    ),
    Files(
        client="madev-id", # 900 (2023016)
        dashboard="202409/DB/madev-id.csv",
        console="202409/console/madev-id.csv",
        output="202409/merge/madev-id.csv",
    ),
    Files(
        client="meval-id", # 900 (2131141257, 2129203678)
        dashboard="202409/DB/meval-id.csv",
        console="202409/console/meval-id.csv",
        output="202409/merge/meval-id.csv",
    ),
    Files(
        client="moladin-collection-id", # 900 (2023015)
        dashboard="202409/DB/moladin-collection-id.csv",
        console="202409/console/moladin-collection-id.csv",
        output="202409/merge/moladin-collection-id.csv",
    ),
    Files(
        client="upperwest-id", # 900 (81377177190)
        dashboard="202409/DB/upperwest-id.csv",
        console="202409/console/upperwest-id.csv",
        output="202409/merge/upperwest-id.csv",
    ),
    Files(
        client="benings-id", # 1500 inbound outbound (2150913442)
        dashboard="202409/DB/benings-id.csv",
        console="202409/console/benings-id.csv",
        output="202409/merge/benings-id.csv",
    ),
    Files(
        client="paragon-id", # 1450 inbound outbound (50913440)
        dashboard="202409/DB/paragon-id.csv",
        console="202409/console/paragon-id.csv",
        output="202409/merge/paragon-id.csv",
    ),
    Files(
        client="rts-id", # 1500 inbound outbound (2150913460)
        dashboard="202409/DB/rts-id.csv",
        console="202409/console/rts-id.csv",
        output="202409/merge/rts-id.csv",
    ),

]
