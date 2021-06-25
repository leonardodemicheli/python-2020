from backpack import Backpack
bp = Backpack()
bp.init_players()
bp.set_name(0, 'alex1')
bp.set_name(1, 'andi1')
bp.add_backpack(0, 'schuhe')
bp.add_backpack(0, 'socken')
print(bp.get_name(0))
print(bp.get_name(1))
print(bp.get_info())
bp.remove_backpack(0, 'schuhe')
print(bp.get_info())

