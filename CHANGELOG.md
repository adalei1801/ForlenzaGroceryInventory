# Inventory Management System Changelog

## Version 1.0 (Initial Release)
- 2020-09-20
- Initial implementation of the inventory management system.
- Features:
  - Add items to the inventory.
  - Remove items from the inventory.

## Version 1.1
- 2021-11-12
- Added user-requested features to improve work-stream productivity
- Features:
  - View the current inventory.
  - Search for items by name.

## Verison 1.2
- 2024-10-17
- System changes to improve interface and work flow as requested by users
- Features:
  - System no longer crashs when sold out item is removed
  - Quantities updates correctly
  - Confirmation question for overwriting an item has been added
  - Current inventory is now printed as the system iterates

## Verison 1.3
- 2024-10-18
- Minor system changes to improve patches from previous verison
- Features:
  - Adding items overwrite fix moved and changed in case user wanted to overwrite
  - Fixed formatting issue by changing price data type to float

## Verison 1.4
- 2024-10-19
- System changes to improve quality of life
- Features:
  - Display inventory option removed
    - Replaced with "update price" function
  - Price can now be updated
    - To update price, press "4"
  - If quantity is set to 0, user can remove it from the inventory
    - If item not removed, it will be labeled as sold out
  - All functions that require existing item name (remove item, update quantity, and update price) now check if item is in inventory
    - If item is not in inventory, user will have to reinput item
  - Formatting improvements
    - Actions are spaced out

## Verison 1.5
- 2024-10-20
- Added new quality of life features
- Features:
  - Groups all update items into single item that leads to sub menu
  - Added update name function