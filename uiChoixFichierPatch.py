from PyQt5.QtWidgets import QGridLayout, QCheckBox, QPushButton, QVBoxLayout, QGroupBox, QDialog

from utils import files_names


class CheckboxWindowFile(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Choix des fichiers à patch')
        self.setGeometry(100, 100, 1200, 600)

        layout = QGridLayout()
        num_rows = [23]
        num_cols = [4]
        nom_checkboxes = files_names

        self.checkboxes = [[]]  # Pour stocker les checkboxes

        check_all_button = []
        uncheck_all_button = []

        for k in range(1):
            group_box = QGroupBox("script")
            group_layout = QGridLayout(group_box)
            for i in range(num_cols[k]):
                for j in range(num_rows[k]):
                    index = i * num_rows[k] + j  # Calcul de l'index pour afficher en colonne
                    if index > len(nom_checkboxes)-1:
                        continue
                    checkbox = QCheckBox(f'{nom_checkboxes[index]}')
                    self.checkboxes[k].append(checkbox)  # Ajouter la checkbox à la liste
                    group_layout.addWidget(checkbox, j, i)

            check_all_button.append(QPushButton('Cocher tout'))
            group_layout.addWidget(check_all_button[k])
            uncheck_all_button.append(QPushButton('Décocher tout'))
            group_layout.addWidget(uncheck_all_button[k])

            group_box.setLayout(group_layout)
            layout.addWidget(group_box)

        check_all_button[0].clicked.connect(self.check_all1)
        uncheck_all_button[0].clicked.connect(self.uncheck_all1)

        ok_button = QPushButton('OK')
        ok_button.clicked.connect(self.ok_clicked)

        button_layout = QVBoxLayout()
        button_layout.addWidget(ok_button)

        main_layout = QVBoxLayout()
        main_layout.addLayout(layout)
        main_layout.addLayout(button_layout)

        self.setLayout(main_layout)

        self.ok_clicked()

    def check_all1(self):
        for checkbox in self.checkboxes[0]:
            checkbox.setChecked(True)

    def uncheck_all1(self):
        for checkbox in self.checkboxes[0]:
            checkbox.setChecked(False)

    def ok_clicked(self):
        self.checkbox_values = []
        for i in range(1):
            self.checkbox_values = [checkbox.isChecked() for checkbox in self.checkboxes[i]]
        self.close()

    def get_checkbox_values(self):
        return self.checkbox_values
