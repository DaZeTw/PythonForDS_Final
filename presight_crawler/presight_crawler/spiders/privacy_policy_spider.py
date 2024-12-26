import scrapy


class PrivacyPolicySpider(scrapy.Spider):
    name = "privacy_policy"
    start_urls = ["https://www.presight.io/privacy-policy.html"]

    def parse(self, response):
        # Select all elements in the order they appear
        elements = response.css('h2, p, li')

        # Prepare content
        content = []

        for element in elements:
            # Get the tag name
            tag_name = element.xpath('name()').get()

            # Process <h2> tags
            if tag_name == 'h2':
                text = element.css('::text').get().strip()
                # Format h2 with uppercase and spacing
                content.append(f"\n{text.upper()}\n")

            # Process <p> tags
            elif tag_name == 'p':
                text = element.css('::text').get().strip()
                content.append(text)

            # Process <li> tags
            elif tag_name == 'li':
                text = element.css('::text').get().strip()
                content.append(f"- {text}")  # Add bullet points for list items

        # Join content into a single text block
        text_output = "\n".join(content)

        # Save to text file
        with open("privacy_policy.txt", "w", encoding="utf-8") as file:
            file.write(text_output)

        yield {"content": text_output}
