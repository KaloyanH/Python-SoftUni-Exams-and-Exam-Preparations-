function solve(input) {
  const rows = input.shift();
  const horses = rows.split("|");


  for (let i = 0; i < input.length; i++) {
    let current = input[i];
    let cmd = current.split(" ");
    if (cmd[0] === "Retake") {
      let nameLeft = cmd[1];
      let nameRight = cmd[2];
      let indexleft = horses.indexOf(nameLeft);
      let indexright = horses.indexOf(nameRight);
      if (indexleft < indexright) {
        horses[indexleft] = nameRight;
        horses[indexright] = nameLeft;
        console.log(nameLeft + " retakes " + nameRight + ".");
      }
    } else if (cmd[0] === "Trouble") {
      let name = cmd[1];
      let index = horses.indexOf(name);
      if (index > 0) {
        let currentName = horses[index];
        let nameBehind = horses[index - 1];
        horses[index] = nameBehind;
        horses[index - 1] = currentName;
        console.log("Trouble for " + currentName + " - drops one position.");
      }
    } else if (cmd[0] === "Rage") {
      let name = cmd[1];
      let index = horses.indexOf(name);
      if (index === horses.length - 1) {
        console.log(name + " rages 2 positions ahead.");
      } else if (index === horses.length - 2) {
        let currentName = horses[index];
        let nameAhead = horses[index + 1];
        horses[index] = nameAhead;
        horses[index + 1] = currentName;
        console.log(name + " rages 2 positions ahead.");
      } else {
        let currentName = horses[index];
        let nameAhead = horses[index + 1];
        let nameAhead2 = horses[index + 1 + 1];
        horses[index + 2] = currentName;
        horses[index + 1] = nameAhead2;
        horses[index] = nameAhead;
        console.log(name + " rages 2 positions ahead.");
      }
    } else if (cmd[0] === "Miracle") {
      let name = horses.shift();
      horses.push(name);
      console.log("What a miracle - " + name + " becomes first.");
    } else if (cmd[0] === "Finish") {
      break;
    }
  }
  console.log(horses.join("->"));
  console.log("The winner is: " + horses.pop());
}
