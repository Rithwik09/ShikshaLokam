function modifyString(s) {
    let charArray = s.split('');

    for (let i = 0; i < charArray.length; i++) {
      let charCode = charArray[i].charCodeAt(0);

      if (charCode % 2 === 0) {
        let nextCharCode = charArray[i + 1] ? charArray[i + 1].charCodeAt(0) + (charCode % 7) : null;

        if (nextCharCode && nextCharCode > 127) {
          nextCharCode = 83;
        }

        if (nextCharCode) {
          charArray[i + 1] = String.fromCharCode(nextCharCode);
        }
      } else {
        let prevCharCode = charArray[i - 1] ? charArray[i - 1].charCodeAt(0) - (charCode % 5) : null;

        if (prevCharCode && prevCharCode < 32) {
          prevCharCode = 83;
        }

        if (prevCharCode) {
          charArray[i - 1] = String.fromCharCode(prevCharCode);
        }
      }
    }

    let result = charArray.join('');

    return result;
  }

  const s = "sHQen}";
  const result = modifyString(s);
  console.log(result);
