# simple-entity-counting
Simple entity counting that count everything provides on a mesh grid upto 35 entities.

### Counting entity.
This script can output a file consist of the number of entity on the first line and their position on the X by Y grid.
## Usage:
+ Prepare a file with this format:
```
X Y
00...010
01...100
........
11...001
```
where X is the map's width and Y is the map's height.
+ Name it `<number>.txt`
+ Run `python run.py <number>` in terminal.

## Disclaimer:
- Diaganol line does not count as a line. Only vertical and horizontal one does.
- Can only count upto 35 Entities (as 1-9 and 26 alphabet letters).
