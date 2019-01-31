var convert = require('xml-js');
var args = process.argv.slice(2);
var xml = require('fs').readFileSync(args[0], 'utf8')
var result = convert.xml2json(xml, {compact: true, spaces: 2,ignoreDeclaration:true});
// console.log(result)

var fs = require('fs');
fs.writeFile("weather.json", result, (err) => {
    if (err) {
        console.error(err);
        return;
    };
    console.log("File has been created");
});