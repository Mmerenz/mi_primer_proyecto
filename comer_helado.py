queres_ir_input = input("¿Queres ir a la cancha? (Si/No):").upper()
tenes_como_ir_input = input("¿Tenes como ir a la cancha? (Si/No):").upper()
tenes_que_estudiar_input = input("¿Tenes que estudiar? (Si/No):" ).upper()
andan_trenes_input = input("¿Funcionan los trenes? (Si/No):").upper()

queres_ir_a_la_cancha = queres_ir_input == "SI"
tenes_como_ir = tenes_como_ir_input == "SI" or andan_trenes_input == "SI"
tenes_que_estudiar = tenes_que_estudiar_input == "NO"

if queres_ir_a_la_cancha and tenes_que_estudiar and tenes_como_ir:
    print("Bueno, vamos")
else:
    print("Bueno, no vamos")
