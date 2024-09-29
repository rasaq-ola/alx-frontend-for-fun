# alx-frontend-for-fun

This repository contains advanced SCSS/Sass tasks for mastering the basics and advanced features of Sass, including variables, mixins, nesting, loops, and media queries.

## Directory Structure
- **0-debug_log.scss**: Prints "Hello world" in debug output.
- **1-color_variable.scss**: Defines a color variable and applies it to `body` and `p`.
- **2-color_variables.scss**: Uses two color variables for text and background.
- **3-nested_tag.scss**: Demonstrates nested declarations for `p` inside `body`.
- **4-nested_class.scss**: Assigns specific text colors based on classes using nested declarations.
- **5-nested_child.scss**: Styles `.red` class as the first child of `body`.
- **6-nested_hover.scss**: Changes button text color on hover.
- **7-nested_deeper.scss**: Applies different font sizes based on the structure of the tags.
- **8-mixin_margins.scss**: Uses mixins to apply margin to `body` and `div`.
- **9-extend_list.scss**: Demonstrates the use of `@extend` for reusing styles.
- **10-import_colors.scss**: Imports variables from another file and applies them.
- **11-loop_photos.scss**: Dynamically generates classes for photos using `@each`.
- **12-loop_header.scss**: Dynamically generates `h*` tags with different font sizes using a loop.
- **100-loop_col.scss**: Creates responsive columns using a loop.
- **101-media_query.scss**: Adjusts font size based on screen width with media queries.
- **102-media_query.scss**: A more advanced media query with multiple breakpoints.
- **103-sort_strings.scss**: Sorts a list of names and prints it using debug.

## Usage
To compile any of the Sass files, run:
```bash
sass <input_file>.scss <output_file>.css

