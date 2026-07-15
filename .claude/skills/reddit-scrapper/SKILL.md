```markdown
# reddit-scrapper Development Patterns

> Auto-generated skill from repository analysis

## Overview
This skill teaches you how to contribute to the `reddit-scrapper` Python codebase, which is designed for scraping Reddit data. You'll learn the project's unique coding conventions, file organization, and how to write and run tests. This guide also provides recommended commands for common development workflows.

## Coding Conventions

### File Naming
- Use **camelCase** for file names.
  - Example: `redditScrapper.py`, `dataParser.py`

### Imports
- Use **relative imports** within the package.
  - Example:
    ```python
    from .utils import fetchData
    ```

### Exports
- Use **named exports** (i.e., define functions/classes and import them explicitly).
  - Example:
    ```python
    # In redditScrapper.py
    def scrapeSubreddit(subreddit):
        pass

    # In another file
    from .redditScrapper import scrapeSubreddit
    ```

### Commit Messages
- Freeform style, no strict prefixes.
- Average length: ~50 characters.
  - Example:  
    ```
    Add function to parse subreddit posts
    ```

## Workflows

### Adding a New Feature
**Trigger:** When implementing new functionality.
**Command:** `/add-feature`

1. Create a new Python file using camelCase (e.g., `newFeature.py`).
2. Implement your feature using relative imports for dependencies.
3. Export functions/classes using named exports.
4. Write or update corresponding test files (`*.test.*`).
5. Commit your changes with a concise, descriptive message.

### Fixing a Bug
**Trigger:** When resolving a bug in the codebase.
**Command:** `/fix-bug`

1. Identify the buggy file and function.
2. Make corrections, following code conventions.
3. Update or add tests to cover the bug fix.
4. Commit with a message describing the fix.

### Running Tests
**Trigger:** To verify code correctness after changes.
**Command:** `/run-tests`

1. Locate test files matching the pattern `*.test.*`.
2. Use the project's preferred (unknown) test runner to execute tests.
3. Review test output and address any failures.

## Testing Patterns

- Test files follow the `*.test.*` naming pattern (e.g., `redditScrapper.test.py`).
- The specific testing framework is unknown; check existing test files for clues.
- Place tests alongside the code or in a dedicated test directory.
- Example test file:
    ```python
    # redditScrapper.test.py
    from .redditScrapper import scrapeSubreddit

    def test_scrapeSubreddit():
        assert scrapeSubreddit('python') is not None
    ```

## Commands
| Command      | Purpose                                    |
|--------------|--------------------------------------------|
| /add-feature | Start the workflow for adding a new feature|
| /fix-bug     | Start the workflow for fixing a bug        |
| /run-tests   | Run all test files in the codebase         |
```
