/**
 * Template Project — core logic.
 *
 * Replace this module with your project's real logic. Keep functions small
 * and pure where possible so they are easy to test.
 */

/**
 * Return a greeting for `name`.
 * @param {string} name
 * @returns {string}
 */
export function greet(name) {
  const cleaned = String(name).trim();
  if (!cleaned) {
    throw new Error("name must not be empty");
  }
  return `Hello, ${cleaned}!`;
}
