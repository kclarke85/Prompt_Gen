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

    def _test_page_load(self) -> None:
        steps = [
            'Given I am on the homepage',
            'Then the page should load within 3 seconds',
            'And all static resources should load successfully'
        ]
        if self.soup.title:
            steps.append(f'And the page title should be "{self.soup.title.string.strip()}"')
        self._add_scenario("Page Load Performance", steps)

    # Other methods for generating test cases omitted for brevity...

def fetch_webpage_content(url: str) -> Tuple[bool, str]:
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        return True, response.text
    except requests.RequestException as e:
        return False, str(e)


def main():
    st.title("QA Test Case Generator")
    st.write("Enter a URL to generate QA test cases:")

    url = st.text_input("Website URL")

    if st.button("Generate Test Cases"):
        is_valid, message = URLValidator.validate(url)
        if not is_valid:
            st.error(message)
        else:
            st.info("Fetching webpage content...")
            success, content = fetch_webpage_content(url)
            if not success:
                st.error(f"Failed to fetch content: {content}")
            else:
                generator = QATestCaseGenerator(content)
                feature_text = generator.generate_feature()
                st.success("Test cases generated successfully!")
                st.text_area("Generated Test Cases", value=feature_text, height=400)


if __name__ == "__main__":
    main()
