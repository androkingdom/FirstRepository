const fs = require("fs")


const manageFile = function (folderDir) {
    fs.appendFile(`${folderDir}/mynewfile1.txt`, , function (err) {
        if (err) throw err;
        console.log('Saved!');
      });
      
}



manageFile("dummyfolder")