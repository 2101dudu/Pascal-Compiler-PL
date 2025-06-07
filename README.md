# Pascal Compiler (Processamento de Linguagens 2025)

A full-featured compiler for the **standard Pascal language**, developed as a practical project for the *Processamento de Linguagens* course at the University of Minho.

This compiler performs **lexical**, **syntactic**, and **semantic analysis**, then translates Pascal code into **machine code** for execution on the [EWVM virtual machine](https://ewvm.epl.di.uminho.pt). It includes a graphical **web-based AST visualizer** to help with debugging and understanding the program structure.

## 📦 Project Structure

```text
.
├── src/                  # Source code for all compiler phases and the web visualizer
│   ├── AST/              # AST-related classes and logic
│   ├── static/           # Frontend assets for the web visualizer
│   ├── templates/        # HTML templates for the Flask app
│   ├── tests/            # Pascal test programs
│   ├── ana_lex.py        # Lexical analyzer
│   ├── ana_sin.py        # Syntactic analyzer
│   ├── ana_sem.py        # Semantic analyzer
│   ├── sin_gen.py        # BNF to Python parser generator
│   ├── prod.txt          # Context-free grammar in BNF
│   ├── gen.py            # Code generator (Pascal to EWVM code)
│   ├── checktree.py      # AST utilities and validation
│   ├── main.py           # Main CLI entry point
│   ├── website.py        # Web visualizer using Flask + D3.js
│   └── test.sh           # Quick tester script
├── assets/               # Project images (e.g. AST preview)
├── docs/                 # Project documentation
│   ├── projeto.pdf       # Official project description
│   └── report.md         # Technical report written by the group
├── LICENSE
└── README.md
```

## 🚀 Features

- **Lexer** using `ply.lex`: identifies keywords, symbols, identifiers, numbers, strings, booleans, etc.
- **Parser** using `ply.yacc`: builds an AST from Pascal grammar (defined in `prod.txt`).
- **Semantic Analyzer**: checks variable declarations, types, scoping rules, array bounds, and more.
- **Code Generator**: translates AST into EWVM machine code.
- **AST Visualizer**: interactive graphical tree using `Flask` and `D3.js`.
- **Test Suite**: several `.pas` programs to validate the compiler functionality.

## 🧪 Running Tests

```bash
cd src/
./test.sh
```

You can also manually run and see the ouput yourself:

```bash
cd src/
cat tests/1.pas | python3 main.py
```

## 🌐 AST Visualizer (Web)

To launch the web visualizer:

```bash
cd src/
python3 -m website
```

Then visit: [http://127.0.0.1:5000](http://127.0.0.1:5000)

Paste any Pascal program into the textarea and view its AST rendered using SVG.

Example:

![AST Example](../assets/ast_preview.png)

## 🛠️ Requirements

- `ply`
- `flask`
- A modern web browser (for AST visualization)

```bash
pip install ply flask
```

## 📝 Authors

- a99890 - [Edgar Ferreira](https://github.com/Edegare)
- a104353 - [Eduardo Faria](https://github.com/2101dudu)
- a104089 - [Nuno Silva](https://github.com/NunoMRS7)

Group 1 - University of Minho, 2025

## 📄 License

This project is licensed under the MIT License. See the [LICENSE](./LICENSE) file for more details.

## 📚 Documentation

Full technical documentation is available in the `docs/` folder:

- [`report.md`](docs/report.md) – complete explanation of the implementation
- [`projeto.pdf`](docs/projeto.pdf) – original project description
