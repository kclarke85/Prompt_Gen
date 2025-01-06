import streamlit as st
import requests
from bs4 import BeautifulSoup
from typing import Tuple, List, Dict
import re
from datetime import datetime


class URLValidator:
    URL_PATTERN = re.compile(
        r'^https?://'
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+[A-Z]{2,6}\.?|'
        r'localhost|'
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'
        r'(?::\d+)?'
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)

    @classmethod
    def validate(cls, url: str) -> Tuple[bool, str]:
        if not url or not url.strip():
            return False, "URL cannot be empty"
        if cls.URL_PATTERN.match(url.strip()):
            return True, "Valid URL"
        return False, "Invalid URL format"


class QATestCaseGenerator:
    def __init__(self, html_content: str):
        self.soup = BeautifulSoup(html_content, 'html.parser')
        self.scenarios: List[Dict] = []
        self.test_case_counter = 1
        self.page_elements = self._collect_page_elements()

    def _collect_page_elements(self) -> Dict:
        return {
            'inputs': self.soup.find_all('input'),
            'buttons': self.soup.find_all('button'),
            'forms': self.soup.find_all('form'),
            'links': self.soup.find_all('a'),
            'dropdowns': self.soup.find_all('select'),
            'checkboxes': self.soup.find_all('input', type='checkbox'),
            'radio_buttons': self.soup.find_all('input', type='radio'),
            'text_areas': self.soup.find_all('textarea'),
            'images': self.soup.find_all('img'),
            'tables': self.soup.find_all('table'),
            'headers': self.soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6'])
        }

    def generate_feature(self) -> str:
        feature_text = [
            "Feature: Web Application QA Test Suite",
            f"  # Generated on {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
            "  As a QA Engineer",
            "  I want to thoroughly test the web application",
            "  So that I can ensure its quality and functionality\n"
        ]

        self._analyze_page()
        for scenario in self.scenarios:
            feature_text.extend(self._format_scenario(scenario))

        return "\n".join(feature_text)

    def _add_scenario(self, name: str, steps: List[str], importance: str = "High") -> None:
        self.scenarios.append({
            'id': f'TC_{str(self.test_case_counter).zfill(3)}',
            'name': name,
            'steps': steps,
            'importance': importance
        })
        self.test_case_counter += 1

    def _format_scenario(self, scenario: Dict) -> List[str]:
        formatted = [
            f"\n  @{scenario['importance']} @{scenario['id']}",
            f"  Scenario: {scenario['name']}",
        ]
        formatted.extend(f"    {step}" for step in scenario['steps'])
        return formatted

    def _analyze_page(self) -> None:
        self._test_page_load()
        self._test_input_fields()
        self._test_buttons()
        self._test_forms()
        self._test_links()
        self._test_dropdowns()
        self._test_checkboxes_radio()
        self._test_text_areas()
        self._test_tables()
        self._test_images()
        self._test_headers()
        self._test_responsive_design()
        self._test_accessibility()
        self._test_error_handling()

    def _test_page_load(self) -> None:
        steps = [
            'Given I am on the homepage',
            'Then the page should load within 3 seconds',
            'And all static resources should load successfully'
        ]
        if self.soup.title:
            steps.append(f'And the page title should be "{self.soup.title.string.strip()}"')
        self._add_scenario("Page Load Performance", steps)

    def _test_input_fields(self) -> None:
        for i, input_field in enumerate(self.page_elements['inputs'], 1):
            input_type = input_field.get('type', 'text')
            input_name = input_field.get('name', f'field_{i}')
            placeholder = input_field.get('placeholder', '')

            steps = [
                'Given I am on the page',
                f'When I locate the {input_type} input field "{input_name}"'
            ]

            if placeholder:
                steps.append(f'Then I should see placeholder text "{placeholder}"')

            if input_type in ['text', 'email', 'password', 'number', 'tel']:
                steps.extend([
                    f'When I enter valid data in the {input_type} field',
                    'Then the input should be accepted',
                    f'When I enter invalid {input_type} format',
                    'Then I should see validation error message'
                ])

            self._add_scenario(f"Input Field Validation - {input_name}", steps, "High")

    def _test_buttons(self) -> None:
        for i, button in enumerate(self.page_elements['buttons'], 1):
            button_text = button.get_text().strip() or f'Button {i}'
            steps = [
                'Given I am on the page',
                f'When I locate the button "{button_text}"',
                'Then the button should be visible and enabled',
                f'When I click the "{button_text}" button',
                'Then the button should respond to the click',
                'And appropriate action should be triggered'
            ]
            self._add_scenario(f"Button Functionality - {button_text}", steps, "High")

    def _test_forms(self) -> None:
        for i, form in enumerate(self.page_elements['forms'], 1):
            steps = ['Given I am on the form page']

            # Test form fields
            for field in form.find_all(['input', 'select', 'textarea']):
                field_name = field.get('name', 'unknown')
                field_type = field.get('type', 'text')
                steps.extend([
                    f'When I locate the {field_type} field "{field_name}"',
                    'Then it should be enabled and interactive'
                ])

            # Test form submission
            steps.extend([
                'When I submit the form with valid data',
                'Then the form should be submitted successfully',
                'When I submit the form with invalid data',
                'Then I should see appropriate validation messages'
            ])

            self._add_scenario(f"Form Validation - Form {i}", steps)

    def _test_links(self) -> None:
        for i, link in enumerate(self.page_elements['links'], 1):
            link_text = link.get_text().strip() or f'Link {i}'
            href = link.get('href', '#')
            steps = [
                'Given I am on the page',
                f'When I locate the link "{link_text}"',
                f'Then the link should point to "{href}"',
                f'When I click the "{link_text}" link',
                'Then I should be redirected correctly'
            ]
            self._add_scenario(f"Link Navigation - {link_text}", steps, "Medium")

    def _test_dropdowns(self) -> None:
        for i, dropdown in enumerate(self.page_elements['dropdowns'], 1):
            options = [opt.get_text().strip() for opt in dropdown.find_all('option')]
            steps = [
                'Given I am on the page',
                f'When I locate dropdown {i}',
                'Then the dropdown should be enabled',
                'When I click the dropdown',
                'Then it should expand and show options'
            ]
            if options:
                steps.append('And the following options should be available:')
                steps.extend(f'  * {option}' for option in options)

            self._add_scenario(f"Dropdown Functionality - Dropdown {i}", steps, "Medium")

    def _test_checkboxes_radio(self) -> None:
        checkboxes = self.page_elements['checkboxes']
        radio_buttons = self.page_elements['radio_buttons']

        if checkboxes:
            steps = [
                'Given I am on the page with checkboxes',
                'Then all checkboxes should be visible',
                'When I click each checkbox',
                'Then they should toggle correctly',
                'And the state should be preserved'
            ]
            self._add_scenario("Checkbox Functionality", steps, "Medium")

        if radio_buttons:
            steps = [
                'Given I am on the page with radio buttons',
                'Then all radio buttons should be visible',
                'When I select different radio options',
                'Then only one option should be selected at a time'
            ]
            self._add_scenario("Radio Button Functionality", steps, "Medium")

    def _test_text_areas(self) -> None:
        for i, textarea in enumerate(self.page_elements['text_areas'], 1):
            steps = [
                'Given I am on the page',
                f'When I locate textarea {i}',
                'Then it should be enabled and empty',
                'When I enter a large text',
                'Then it should handle the input correctly',
                'And show scrollbars if needed'
            ]
            self._add_scenario(f"Textarea Functionality - {i}", steps, "Medium")

    def _test_tables(self) -> None:
        for i, table in enumerate(self.page_elements['tables'], 1):
            steps = [
                'Given I am on the page',
                f'When I locate table {i}',
                'Then the table should be properly formatted',
                'And all cells should be properly aligned',
                'And data should be correctly displayed'
            ]
            self._add_scenario(f"Table Display - Table {i}", steps, "Medium")

    def _test_images(self) -> None:
        for i, img in enumerate(self.page_elements['images'], 1):
            alt_text = img.get('alt', '')
            src = img.get('src', '')
            steps = [
                'Given I am on the page',
                f'When I locate image {i}',
                'Then the image should load correctly',
                f'And have alt text "{alt_text}"',
                f'And source should be "{src}"'
            ]
            self._add_scenario(f"Image Display - Image {i}", steps, "Medium")

    def _test_headers(self) -> None:
        headers = [(h.name, h.get_text().strip()) for h in self.page_elements['headers']]
        if headers:
            steps = ['Given I am on the page']
            for tag, text in headers:
                steps.append(f'Then I should see {tag} header "{text}"')
            self._add_scenario("Header Structure", steps, "Low")

    def _test_responsive_design(self) -> None:
        viewports = [
            ('desktop', '1920x1080'),
            ('tablet', '768x1024'),
            ('mobile', '375x667')
        ]

        for device, size in viewports:
            steps = [
                f'Given I am viewing the page on {device} ({size})',
                'Then all elements should be properly aligned',
                'And content should be readable',
                'And navigation should be accessible'
            ]
            self._add_scenario(f"Responsive Design - {device}", steps, "High")

    def _test_accessibility(self) -> None:
        steps = [
            'Given I am testing accessibility',
            'Then all images should have alt text',
            'And all form fields should have labels',
            'And color contrast should meet WCAG standards',
            'And keyboard navigation should work properly',
            'And ARIA attributes should be properly set'
        ]
        self._add_scenario("Accessibility Compliance", steps, "High")

    def _test_error_handling(self) -> None:
        steps = [
            'Given I am testing error handling',
            'When I perform invalid actions',
            'Then I should see appropriate error messages',
            'And the messages should be clearly visible',
            'And the application should recover gracefully'
        ]
        self._add_scenario("Error Handling", steps, "High")


def main() -> None:
    # Page configuration
    st.set_page_config(
        page_title="QA Test Case Generator",
        page_icon="https://120water.com/wp-content/uploads/2020/05/120WaterAudit_Logo_2C_RGB-1.png"
    )

    # Add header image
    st.image(
        "https://images.pexels.com/photos/9749/hands-water-poor-poverty.jpg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1",
        use_column_width=True)

    st.title("QA Test Case Generator")
    st.markdown("Generate comprehensive QA test cases from web pages")

    url = st.text_input("Enter webpage URL:", help="Enter a valid webpage URL")

    if st.button("Generate Test Cases"):
        if not url:
            st.error("Please enter a URL")
            return

        is_valid, message = URLValidator.validate(url)
        if not is_valid:
            st.error(message)
            return

        try:
            with st.spinner("Analyzing webpage and generating test cases..."):
                response = requests.get(url, timeout=10)
                response.raise_for_status()

                generator = QATestCaseGenerator(response.text)
                test_cases = generator.generate_feature()

                st.header("Generated Test Cases")
                st.code(test_cases, language="gherkin")




                st.download_button(
                    label="Download Test Cases",
                    data=test_cases,
                    file_name="qa_test_cases.feature",
                    mime="text/plain"
                )

        except requests.Timeout:
            st.error("Request timed out. Please try again.")
        except requests.RequestException as e:
            st.error(f"Error fetching URL: {str(e)}")
        except Exception as e:
            st.error(f"Unexpected error: {str(e)}")


if __name__ == "__main__":
    main()