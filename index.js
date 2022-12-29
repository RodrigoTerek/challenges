// function rabbit(n) {
//     if (n < 3)
//         return n;
//     return rabbit(n - 1) + rabbit(n - 2);
// }

// for (let i = 0; i < 10; i++) {
//     console.log(rabbit(i))
// }

// let arr = [4, 7, 1, -3, 2];

// function findSum(k) {
//   for (let i = 0; i < arr.length; i++)
//     for (let j = i; j < arr.length; j++)
//       if (arr[i] + arr[j] == k) return true;
//   return false;
// }

// console.log(findSum(10));

// function allValuesFromHeight(root, height, currentHeight = 1, acc = []) {
//   if (height == currentHeight) return [...acc, root.value];

//   if (!root.left && !root.right) return acc;

//   let leftResult = [];
//   let rightResult = [];

//   if (root.left)
//     leftResult = allValuesFromHeight(root.left, height, currentHeight + 1, acc);

//   if (root.right)
//     rightResult = allValuesFromHeight(
//       root.right,
//       height,
//       currentHeight + 1,
//       acc
//     );

//   return [...acc, ...leftResult, ...rightResult];
// }

// function node(n, left, right) {
//   this.value = n;
//   this.left = left;
//   this.right = right;
// }

// const root = new node(1, new node(2, new node(3)), new node(4, new node(5), new node(6)))
// console.log(allValuesFromHeight(root, 5));

// function sortColors(arr) {
//   let result = [];
//   let [red, white, blue] = [0, 0, 0];

//   for (const color of arr) {
//     switch (color) {
//       case 0:
//         red++;
//         break;
//       case 1:
//         white++;
//         break;
//       case 2:
//         blue++;
//         break;
//     }
//   }

//   console.log({ red, white, blue });
//   while (red + white + blue > 0) {
//     if (red) {
//       result.push(0);
//       red--;
//     } else if (white) {
//       result.push(1);
//       white--;
//     } else if (blue) {
//       result.push(2);
//       blue--;
//     }
//   }

//   return result;
// }

// console.log(sortColors([0, 1, 2, 2, 1, 1, 2, 2, 0, 0, 0, 0, 2, 1]));

function calcClockAngle(hours, minutes) {
  const hoursPos = ((hours % 12) + minutes) / 60 * 30;
  const minutesPos = (minutes / 5) * 30;

  return Math.abs(hoursPos - minutesPos);
}

console.log(calcClockAngle(12, 30));
