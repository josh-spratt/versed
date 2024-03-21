import requests
import typer
from dataclasses import dataclass
import os

app = typer.Typer()


@app.command()
def init():
    if os.path.exists(".versed"):
        print("Versed configuration has already been initialized.")
    else:
        with open(".versed", "w") as f:
            pass
        print("Initialized new Versed configuration file.")


@app.command()
def select_verse(scripture_reference: str):
    url_str = f"https://api.esv.org/v3/passage/text/?q={scripture_reference.replace(' ', '+')}"
    if os.path.exists(".versed"):
        with open(".versed", "r") as f:
            token = f.read()
        headers = {"Authorization": token}
        res = requests.get(url=url_str, headers=headers)
        print(res.text)
    else:
        print("""No Versed configuration found. Please run python -m versed init and put your API token in the .versed
        configuration file that is created""")
    # curl -s -H $ESV_API_TOKEN 'https://api.esv.org/v3/passage/text/?q=Psalm+27:4' | jq '.passages[0]' -r
    # sample payload:
    # data = {
    #     "query": "Psalm 27:4",
    #     "canonical": "Psalm 27:4",
    #     "parsed": [[19027004, 19027004]],
    #     "passage_meta": [
    #         {
    #             "canonical": "Psalm 27:4",
    #             "chapter_start": [19027001, 19027014],
    #             "chapter_end": [19027001, 19027014],
    #             "prev_verse": 19027003,
    #             "next_verse": 19027005,
    #             "prev_chapter": [19026001, 19026012],
    #             "next_chapter": [19028001, 19028009],
    #         }
    #     ],
    #     "passages": [
    #         "Psalm 27:4\n\n    [4] One thing have I asked of the LORD,\n        that will I seek after:\n    that I may dwell in the house of the LORD\n        all the days of my life,\n    to gaze upon the beauty of the LORD\n        and to inquire(1) in his temple.\n    \n\nFootnotes\n\n(1) 27:4 Or *meditate*\n (ESV)"
    #     ],
    # }


if __name__ == "__main__":
    app()
