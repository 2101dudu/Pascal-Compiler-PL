from flask import Flask, render_template, request, jsonify
from ana_sin import parse_pascal

app = Flask(__name__)


def astnode_to_dict(node):
    """
    Recursively convert an ASTNode (or list/leaf) into a JSON-serializable dict
    with a guaranteed `children` list.
    """
    # 1) None → a dummy node
    if node is None:
        return {"name": "None", "children": []}

    # 2) Strings or numbers → leaves
    if isinstance(node, (str, int, float)):
        return {"name": str(node), "children": []}

    # 4) Otherwise it should be your ASTNode
    name = node.value or ""
    children = [astnode_to_dict(c) for c in node.children]
    return {"name": name, "children": children}


@app.route('/', methods=['GET', 'POST'])
def index():
    # Renders the main page with an optional tree
    tree_data = None
    if request.method == 'POST':
        pascal_code = request.form.get('code', '')
        # Feed the code into your PLY-based parser to get the AST root
        root = parse_pascal(pascal_code)
        tree_data = astnode_to_dict(root)
    return render_template('index.html', tree_data=tree_data)


@app.route('/api/tree', methods=['POST'])
def api_tree():
    # API endpoint that returns JSON AST for a given Pascal snippet
    payload = request.get_json() or {}
    pascal_code = payload.get('code', '')
    root = parse_pascal(pascal_code)
    return jsonify(astnode_to_dict(root))


if __name__ == '__main__':
    # For development; in production use a proper WSGI server
    app.run(debug=True, port=5000)
