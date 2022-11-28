#!/usr/bin/node
const lang = 'C is fun\nPython is cool\nJavaScript is amazing';

for (const arg in lang) {
    console.log(lang[arg]);
}
