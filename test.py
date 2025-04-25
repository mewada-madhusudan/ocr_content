from pdf_craft import PDFPageExtractor, MarkDownWriter
import datetime

start_time = datetime.datetime.now()
extractor = PDFPageExtractor(
    device="cpu",  # If you want to use CUDA, please change to device="cuda" format.
    model_dir_path=r"D:/test/model",  # The folder address where the AI ​​model is downloaded and installed
)
markdown_path = r"D:/test/test2.md"
with MarkDownWriter(markdown_path, "images", "utf-8") as md:
    for block in extractor.extract(pdf=r"21583473018.pdf"):
        md.write(block)
print(datetime.datetime.now() - start_time)
start_time = datetime.datetime.now()

from pdf_craft import OCRLevel, PDFPageExtractor

extractor = PDFPageExtractor(
    device="cpu",
    model_dir_path=r"D:/test/model",
    ocr_level=OCRLevel.OncePerLayout,
)

markdown_path = r"D:/test/test_multiple.md"
with MarkDownWriter(markdown_path, "images", "utf-8") as md:
    for block in extractor.extract(pdf=r"21583473018.pdf"):
        md.write(block)

print(datetime.datetime.now() - start_time)
