package armory.logicnode;

class PrintNode extends LogicNode {

	public function new(tree:LogicTree) {
		super(tree);
	}

	override function run() {
		var value:Dynamic = inputs[1].get();
	
		trace(value);

		super.run();
	}
}
