import pytest
from typing import Optional

# --- Core Utility Component Under Test ---
class TitleValidator:
    """
    A utility class responsible for validating and sanitizing titles, 
    specifically handling potential constraints imposed by ultra-long strings.
    """
    MAX_LENGTH = 512  # Standard API limit assumption for a platform like this

    @staticmethod
    def sanitize(title: Optional[str]) -> str:
        """Cleans the title of leading/trailing whitespace."""
        if not isinstance(title, str):
            return ""
        return title.strip()

    @classmethod
    def validate_and_truncate(cls, raw_title: Optional[str], enforce_limit: bool = True) -> str:
        """
        Validates the input against length constraints and truncates if necessary.

        Args:
            raw_title: The potentially massive string title.
            enforce_limit: If True, the title is truncated if it exceeds MAX_LENGTH. 
                           If False, an error/warning state should be preferred in real life.

        Returns:
            The processed and length-constrained title.

        Raises:
            ValueError: If the title is excessively invalid or fundamentally too long 
                        and enforcement is not configured to handle it.
        """
        # 1. Input Sanitization and Type Check
        if raw_title is None:
            return ""
        
        sanitized_title = TitleValidator.sanitize(raw_title)

        # Handle the empty string case early
        if not sanitized_title:
            return ""

        # 2. Length Validation and Handling
        if len(sanitized_title) > cls.MAX_LENGTH:
            print(f"--- WARNING: Title length ({len(sanitized_title)} chars) exceeds limit ({cls.MAX_LENGTH}). ---")
            
            if enforce_limit:
                # Truncation strategy: We truncate and add an ellipsis to indicate clipping, 
                # but we must ensure the resulting string is exactly MAX_LENGTH or less.
                truncated = sanitized_title[:cls.MAX_LENGTH - 3] + "..."
                return truncated
            else:
                # If enforcement is off, treat this as a fatal structural error for testing purposes
                raise ValueError(f"Title exceeds maximum length of {cls.MAX_LENGTH} characters.")

        return sanitized_title


# ==================================================
# PYTEST UNIT TESTS FOR EDGE CASE COVERAGE
# ==================================================

class TestTitleValidator:

    def test_1_standard_short_titles(self):
        """Test standard, valid, short titles."""
        assert TitleValidator.validate_and_truncate("A simple title", enforce_limit=True) == "A simple title"
        assert TitleValidator.validate_and_truncate("Another normal heading", enforce_limit=True) == "Another normal heading"

    def test_2_boundary_conditions_whitespace(self):
        """Test cleaning of leading and trailing whitespace."""
        raw = "  \n  A very spaced out title! \t \r\n"
        expected = "A very spaced out title!"
        assert TitleValidator.validate_and_truncate(raw, enforce_limit=True) == expected

    def test_3_edge_case_empty_string(self):
        """Test handling of empty input strings."""
        assert TitleValidator.validate_and_truncate("", enforce_limit=True) == ""
        assert TitleValidator.validate_and_truncate("   ", enforce_limit=True) == ""

    def test_4_edge_case_null_input(self):
        """Test handling of None input."""
        # We must explicitly check the validation logic handles None safely
        # Note: In real type-hinted code, this might raise a TypeError before reaching validate_and_truncate.
        assert TitleValidator.validate_and_truncate(None, enforce_limit=True) == ""

    def test_5_boundary_exactly_at_max_length(self):
        """Test title length exactly matching the defined MAX_LENGTH (512 chars)."""
        # Create a string of 512 'A' characters
        long_string = 'A' * TitleValidator.MAX_LENGTH
        assert len(TitleValidator.validate_and_truncate(long_string, enforce_limit=True)) == TitleValidator.MAX_LENGTH
        
    def test_6_boundary_just_under_max_length(self):
        """Test title length just under the defined MAX_LENGTH (e.g., 510 chars)."""
        # Create a string of 510 'B' characters
        long_string = 'B' * (TitleValidator.MAX_LENGTH - 2)
        assert len(TitleValidator.validate_and_truncate(long_string, enforce_limit=True)) == TitleValidator.MAX_LENGTH - 2

    def test_7_violation_exceeding_max_length_truncation(self):
        """Test title significantly exceeding MAX_LENGTH and confirming proper truncation."""
        # Create a string of 600 'X' characters
        excessive_string = 'X' * (TitleValidator.MAX_LENGTH + 88)

        result = TitleValidator.validate_and_truncate(excessive_string, enforce_limit=True)
        
        # Check that the resulting string length is exactly MAX_LENGTH due to truncation and ellipsis
        assert len(result) == TitleValidator.MAX_LENGTH
        
        # Check that the required ellipses are present at the end (for safety/UX)
        assert result.endswith("...")

    def test_8_violation_exceeding_max_length_disabling_enforcement(self):
        """Test what happens when enforcement is disabled for an overly long title."""
        excessive_string = 'Z' * (TitleValidator.MAX_LENGTH + 1)

        # Expect the function to raise a ValueError as designed in the utility class
        with pytest.raises(ValueError) as excinfo:
            TitleValidator.validate_and_truncate(excessive_string, enforce_limit=False)
        
        assert "exceeds maximum length" in str(excinfo.value)

    def test_9_unicode_and_emoji_coverage(self):
        """Test that complex Unicode characters and emojis are counted correctly."""
        # Title containing mixed English, CJK characters (3 bytes), and Emojis (often 1-4 bytes).
        complex_title = "✨Title with a lot of amazing 🎉 unicode content! こんにちは🌍🚀"
        expected_cleaned = complex_title.strip()
        
        assert TitleValidator.validate_and_truncate(complex_title, enforce_limit=True) == expected_cleaned

    @pytest.mark.parametrize("raw_input, expected_result", [
        # Case: None input
        (None, ""), 
        # Case: Pure whitespace
        (" \t\r\n ", ""),
        # Case: Empty string
        ("", "")
    ])
    def test_10_combined_validation_edge_cases(self, raw_input, expected_result):
        """Parameterized test for combining various invalid/empty inputs."""
        assert TitleValidator.validate_and_truncate(raw_input, enforce_limit=True) == expected_result