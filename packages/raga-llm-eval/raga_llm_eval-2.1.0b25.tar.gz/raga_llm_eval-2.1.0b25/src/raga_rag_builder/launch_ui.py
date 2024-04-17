import subprocess


def main():
    subprocess.run(
        [
            "streamlit",
            "run",
            "raga_rag_builder/raga_rag_builder_ui.py",
        ]
    )


if __name__ == "__main__":
    main()
