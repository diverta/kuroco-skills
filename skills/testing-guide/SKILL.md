---
name: testing-guide
description: Guide for writing Kuroco tests using PHPUnit/Codeception. Use this skill when asked to write tests, create test files, or when working with unit/integration tests in this codebase.
---

# Testing Guide

## Unit Test vs Integration Test

### Unit Test
- **Purpose:** Tests one small piece of code in isolation (like a single function)
- **Example:** "Does my math function add numbers correctly?"
- **Dependencies:** Use **fake versions (mocks)** so the test is fast and isolated

### Integration Test
- **Purpose:** Tests how different parts of your code work together
- **Example:** "Does my code save data to the database and then read it back correctly?"
- **Dependencies:** Often uses **real versions** (like a test database)

**Note:** These are guidelines, not strict rules. Use your best judgment—sometimes a unit test might use a real (but simple) database if it's easier.

## Test File Organization

### Small Classes
Put all tests in one test file.
- `MyCode.php` → `MyCodeTest.php`

### Large Classes or Complex Methods
Split tests into smaller, focused files by feature or scenario.

**Example:** For a `TopicsList` class testing `run()`:
```
/nfs/tests/src/Testcase/Opendev/Unit/modules/topics/topics_list/run/
├── TopicsListBasicTest.php
├── TopicsListFavoriteCommentTest.php
├── TopicsListFilteringTest.php
├── TopicsListOrderingTest.php
├── TopicsListPaginationTest.php
├── TopicsListSecurityTest.php
└── TopicsListSpecialCasesTest.php
```

## Writing Tests: AAA Pattern

Always follow **Arrange-Act-Assert**:

1. **Arrange:** Set up preconditions—create objects, prepare mock/real data, set up stubs
2. **Act:** Execute the specific code being tested (single, clear action)
3. **Assert:** Verify the outcome using PHPUnit/Codeception assertions

## Test Style Requirements

- **No control flow in tests:** Avoid `if` statements, loops, `try-catch` (unless testing exceptions)
- **Use Mockery** for mocking when needed
- **Use BDD style:** Write tests using `$this->describe()` and `$this->it()` syntax
- **Be consistent:** Follow the patterns in existing tests

## BDD Assertions: Use `codeception/verify` as the API reference

When writing BDD-style expectations (e.g. `verify(...)`, `expect(...)`, and chained matchers), **avoid guessing matcher method names**. Instead, treat the upstream `codeception/verify` expectation classes as the source of truth for available methods and behavior:

- `Kuroco-opendev/nfs/lib/vendor/codeception/verify/src/Codeception/Verify/Expectations/ExpectMixed.php`
- `Kuroco-opendev/nfs/lib/vendor/codeception/verify/src/Codeception/Verify/Expectations/ExpectAny.php`

## Example Test Structure
```php
public function testSomethingWorks(): void
{
    $this->describe('ClassName', function () {
        $this->it('should do expected behavior', function () {
            // Arrange
            $dependency = Mockery::mock(Dependency::class);
            $subject = new MyClass($dependency);
            
            // Act
            $result = $subject->doSomething();
            
            // Assert
            $this->assertEquals('expected', $result);
        });
    });
}
```
