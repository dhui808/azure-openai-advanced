import azure.cognitiveservices.speech as speechsdk
import os
from dotenv import load_dotenv
from azure.identity import DefaultAzureCredential
load_dotenv()

def display_image(filepath):
    from IPython.display import Image
    return Image(filename=filepath)
    
def _in_span(word, spans):
    for span in spans:
        if word.span.offset >= span.offset and (word.span.offset + word.span.length) <= (span.offset + span.length):
            return True
    return False

def _format_polygon(polygon):
    if not polygon:
        return "N/A"
    return ", ".join([f"[{polygon[i]}, {polygon[i + 1]}]" for i in range(0, len(polygon), 2)])


def analyze_read():
    path_to_sample_documents = "./Form_1.jpg"

    from azure.core.credentials import AzureKeyCredential
    from azure.ai.documentintelligence import DocumentIntelligenceClient

    endpoint = os.environ["AZURE_FORM_RECOGNIZER_ENDPOINT"]
    # key = os.environ["AZURE_FORM_RECOGNIZER_KEY"]

    document_analysis_client = DocumentIntelligenceClient(
        endpoint=endpoint, credential=DefaultAzureCredential()
    )
    with open(path_to_sample_documents, "rb") as f:
        poller = document_analysis_client.begin_analyze_document(
            "prebuilt-read", body=f
        )
    result = poller.result()

    print("----Languages detected in the document----")
    if result.styles and any([style.is_handwritten for style in result.styles]):
        print("Document contains handwritten content")
    else:
        print("Document does not contain handwritten content")

    for page in result.pages:
        print(f"----Analyzing layout from page #{page.page_number}----")
        print(f"Page has width: {page.width} and height: {page.height}, measured with unit: {page.unit}")

        if page.lines:
            for line_idx, line in enumerate(page.lines):
                words = []
                if page.words:
                    for word in page.words:
                        print(f"......Word '{word.content}' has a confidence of {word.confidence}")
                        if _in_span(word, line.spans):
                            words.append(word)
                print(
                    f"...Line # {line_idx} has word count {len(words)} and text '{line.content}' "
                    f"within bounding polygon '{_format_polygon(line.polygon)}'"
                )

        if page.selection_marks:
            for selection_mark in page.selection_marks:
                print(
                    f"Selection mark is '{selection_mark.state}' within bounding polygon "
                    f"'{_format_polygon(selection_mark.polygon)}' and has a confidence of {selection_mark.confidence}"
                )

    if result.paragraphs:
        print(f"----Detected #{len(result.paragraphs)} paragraphs in the document----")
        # Sort all paragraphs by span's offset to read in the right order.
        result.paragraphs.sort(key=lambda p: (p.spans.sort(key=lambda s: s.offset), p.spans[0].offset))
        print("-----Print sorted paragraphs-----")
        for paragraph in result.paragraphs:
            if not paragraph.bounding_regions:
                print(f"Found paragraph with role: '{paragraph.role}' within N/A bounding region")
            else:
                print(f"Found paragraph with role: '{paragraph.role}' within")
                print(
                    ", ".join(
                        f" Page #{region.page_number}: {_format_polygon(region.polygon)} bounding region"
                        for region in paragraph.bounding_regions
                    )
                )
            print(f"...with content: '{paragraph.content}'")
            print(f"...with offset: {paragraph.spans[0].offset} and length: {paragraph.spans[0].length}")

    if result.tables:
        for table_idx, table in enumerate(result.tables):
            print(f"Table # {table_idx} has {table.row_count} rows and " f"{table.column_count} columns")
            if table.bounding_regions:
                for region in table.bounding_regions:
                    print(
                        f"Table # {table_idx} location on page: {region.page_number} is {_format_polygon(region.polygon)}"
                    )
            for cell in table.cells:
                print(f"...Cell[{cell.row_index}][{cell.column_index}] has text '{cell.content}'")
                if cell.bounding_regions:
                    for region in cell.bounding_regions:
                        print(
                            f"...content on page {region.page_number} is within bounding polygon '{_format_polygon(region.polygon)}'"
                        )

    print("----------------------------------------")

display_image("./Form_1.jpg")
analyze_read()
