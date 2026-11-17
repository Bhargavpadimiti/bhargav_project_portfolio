import assert from "node:assert/strict";
import { test } from "node:test";

import { greet } from "../src/index.js";

test("greet returns a greeting", () => {
  assert.equal(greet("Ada"), "Hello, Ada!");
});

test("greet strips whitespace", () => {
  assert.equal(greet("  Ada  "), "Hello, Ada!");
});

test("greet rejects an empty name", () => {
  assert.throws(() => greet("   "), /must not be empty/);
});
