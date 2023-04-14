def on_board(new_place: tuple) -> bool:
    if all(0 < place <= 8 for place in new_place):
        print("Да, вы на доске")
        return True
    else:
        print('Вы вышли за пределы доски и собственной наглости')
        return False


class Chessmen:
    place: tuple = (4, 5)
    _is_white = True

    def change_color(self) -> None:
        self._is_white = not self._is_white

    def change_place(self, new_place: tuple) -> None:
        if on_board(new_place):
            self.place = new_place

    def can_move(self, new_place: tuple) -> bool:
        raise NotImplementedError

    def info(self) -> str:
        return f'Место на доске: {self.place}, цвет фигуры: {self._is_white}'


class Queen(Chessmen):
    def can_move(self, new_place: tuple) -> bool:
        if not on_board(new_place):
            return False
        the_x, the_y = self.place
        new_x, new_y = new_place
        diagonal = abs(new_x - old_x) == abs(new_y - old_y)
        delta = new_x == old_x or new_y == old_y
        return delta or diagonal


class King(Chessmen):
    def can_move(self, new_place: tuple):
        if not on_board(new_place):
            return False
        the_x, the_y = self.place
        new_x, new_y = new_place
        return abs(new_x - the_x) <= 1 and abs(new_y - the_y) <= 1


class Knight(Chessmen):
    def can_move(self, new_place: tuple):
        if not on_board(new_place):
            return False
        the_x, the_y = self.place
        possible_place = the_x - 2, the_y - 1 or the_x - 1, the_y - 2
        possible_place = new_place
        self.place = possible_place
        return possible_place


class Bishop(Chessmen):
    def can_move(self, new_place: tuple):
        if not on_board(new_place):
            return False
        the_x, the_y = self.place
        new_x, new_y = new_place
        return abs(new_x - the_x) == abs(new_y - the_y)


class Rook(Chessmen):
    def can_move(self, new_place: tuple):
        if not on_board(new_place):
            return False
        the_x, the_y = self.place
        new_x, new_y = new_place
        return new_x == the_x or new_y == the_y


class Pawn(Chessmen):
    def can_move(self, new_place: tuple):
        if not on_board(new_place):
            return False
        the_x, the_y = self.place
        new_x, new_y = new_place
        return (self._is_white and new_y == the_y + 1 and new_x == the_x) or (
                not self._is_white and new_y == the_y - 1 and new_x == the_x)


def chessmen_list(checking_chessmen: [Chessmen], new_place: tuple):
    return [chessman for chessman in checking_chessmen if chessman.can_move(new_place)]


queen1 = Queen()
king1 = King()
knight1 = Knight()
bishop1 = Bishop()
rook1 = Rook()
pawn1 = Pawn()
queen2 = Queen()
king2 = King()
knight2 = Knight()
bishop2 = Bishop()
rook2 = Rook()
pawn2 = Pawn()

queen1.change_place((5, 90))
king1.change_place((1, 1))
knight1.change_place((5, 6))
bishop1.change_place((3, 3))
rook1.change_place((4, 8))
pawn1.change_place((5, 6))
pawn2.change_color()
pawn2.change_place((5, 6))

chessmen = [pawn1, pawn2, queen1, queen2, king1, king2, bishop1, bishop2, rook1, rook2, knight1, knight2]

result = chessmen_list(chessmen, (3, 4))
