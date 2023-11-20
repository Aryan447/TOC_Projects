function dfa(string) {
    const states = new Set(["A", "B", "C"]);
    const transitions = {
      A: { "0": "B", "1": "A" },
      B: { "0": "C", "1": "A" },
      C: { "0": "C", "1": "A" },
    };
    const finalStates = new Set(["C"]);
  
    let currentState = "A";
    for (let c of string) {
      currentState = transitions[currentState][c];
    }
  
    if (finalStates.has(currentState)) {
      return true;
    } else {
      return false;
    }
  }
  
  function main() {
    const string = prompt("Enter a string: ");
    if (dfa(string)) {
      console.log("ACCEPTED");
    } else {
      console.log("NOT ACCEPTED");
    }
  }
  
  main();
  