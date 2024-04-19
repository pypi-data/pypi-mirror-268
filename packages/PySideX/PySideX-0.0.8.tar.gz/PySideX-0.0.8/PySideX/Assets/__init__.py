import os


class Assets:
    class svg:
        pysidex = os.path.join(
            os.path.dirname(os.path.abspath(__file__)), "svg", "pysidex.svg"
        )

    class ico:
        pysidex = os.path.join(
            os.path.dirname(os.path.abspath(__file__)), "ico", "pysidex.ico"
        )
