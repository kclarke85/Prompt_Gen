import streamlit as st
import requests
from bs4 import BeautifulSoup
from typing import Tuple, List, Dict
import re
from datetime import datetime

# This must be the first and only st.set_page_config() call
st.set_page_config(
    page_title="QA Test Case Generator",
    page_icon="🧊",
    menu_items={
        'Get Help': None,
        'Report a bug': None,
        'About': None
    }
)

# Hide Streamlit elements
hide_streamlit_style = """
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}
</style>
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)


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
        self._test_navigation()
        self._test_forms()
        self._test_dynamic_elements()
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

    def _test_navigation(self) -> None:
        nav_links = self.soup.find_all('a')
        if nav_links:
            for i, link in enumerate(nav_links, 1):
                steps = [
                    'Given I am on the homepage',
                    f'When I click on the link "{link.get_text().strip()}"',
                    'Then I should be redirected to the correct page',
                    'And the page should load successfully',
                    'When I click the browser back button',
                    'Then I should return to the homepage'
                ]
                self._add_scenario(f"Navigation Flow - Link {i}", steps, "Medium")

    def _test_forms(self) -> None:
        forms = self.soup.find_all('form')
        for i, form in enumerate(forms, 1):
            steps = ['Given I am on the page with the form']

            inputs = form.find_all(['input', 'textarea', 'select'])
            for input_elem in inputs:
                input_type = input_elem.get('type', 'text')
                input_name = input_elem.get('name', '')
                if input_type and input_name:
                    steps.extend([
                        f'When I enter valid data in the "{input_name}" field',
                        f'Then the "{input_name}" field should accept the input'
                    ])

                    if input_type in ['email', 'number', 'tel']:
                        steps.extend([
                            f'When I enter invalid data in the "{input_name}" field',
                            'Then I should see a validation error message'
                        ])

            steps.extend([
                'When I submit the form with valid data',
                'Then the form should be submitted successfully',
                'And I should see a success message'
            ])
            self._add_scenario(f"Form Validation - Form {i}", steps)

    def _test_dynamic_elements(self) -> None:
        dynamic_elements = self.soup.find_all(['button', 'select', 'details'])
        if dynamic_elements:
            steps = [
                'Given I am on the page',
                'When I interact with dynamic elements',
                'Then they should respond appropriately',
                'And any loading spinners should be displayed during data fetching',
                'And the UI should update without page refresh'
            ]
            self._add_scenario("Dynamic Content Behavior", steps)

    def _test_responsive_design(self) -> None:
        steps = [
            'Given I am testing responsive design',
            'When I view the page on a desktop viewport (1920x1080)',
            'Then all elements should be properly aligned',
            'When I view the page on a tablet viewport (768x1024)',
            'Then the layout should adapt appropriately',
            'When I view the page on a mobile viewport (375x667)',
            'Then the content should be properly stacked',
            'And all text should be readable',
            'And touch targets should be adequately sized'
        ]
        self._add_scenario("Responsive Design Validation", steps)

    def _test_accessibility(self) -> None:
        steps = [
            'Given I am testing accessibility',
            'Then all images should have alt text',
            'And all form fields should have proper labels',
            'And the page should have proper heading hierarchy',
            'And color contrast should meet WCAG standards',
            'And all interactive elements should be keyboard accessible'
        ]
        self._add_scenario("Accessibility Compliance", steps)

    def _test_error_handling(self) -> None:
        forms = self.soup.find_all('form')
        if forms:
            steps = [
                'Given I am testing error handling',
                'When I submit a form with invalid data',
                'Then I should see appropriate error messages',
                'And the error messages should be clearly visible',
                'And the form should not be submitted',
                'When I correct the errors',
                'And submit the form again',
                'Then the form should be submitted successfully'
            ]
            self._add_scenario("Error Handling", steps)


def main() -> None:
    # Add header image
    st.image(
        "https://images.pexels.com/photos/9749/hands-water-poor-poverty.jpg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1",
        use_container_width=True
    )

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
