//============================================================================
// Name        : wizardui.h
// Author      : Antonius Torode
// Date        : 5-17-2018
// Copyright   : This file can be used under the conditions of Antonius' 
//				 General Purpose License (AGPL).
// Description : Header file for wizardui.cpp.
//============================================================================

#ifndef WIZARDUI_H
#define WIZARDUI_H

#include <QMainWindow>
#include <string>

using std::string;

namespace Ui {
	class WizardUI;
}

class WizardUI : public QMainWindow{
    Q_OBJECT

public:
    explicit WizardUI(QWidget *parent = 0);
    ~WizardUI();

private slots:
    void on_levelModifier_plus_clicked();
    void on_levelModifier_minus_clicked();
	
    void on_strengthModifier_plus_clicked();
    void on_strengthModifier_minus_clicked();
    void on_dexterityModifier_plus_clicked();
    void on_dexterityModifier_minus_clicked();
    void on_constitutionModifier_plus_clicked();
    void on_constitutionModifier_minus_clicked();
    void on_intelligenceModifier_plus_clicked();
    void on_intelligenceModifier_minus_clicked();
	void on_wisdomModifier_plus_clicked();
    void on_wisdomModifier_minus_clicked();
	void on_charismaModifier_plus_clicked();
    void on_charismaModifier_minus_clicked();
	void on_abilityModifier_all_clicked();

	//Ability score checks.
    void on_strengthModifier_check_clicked();
    void on_dexterityModifier_check_clicked();
    void on_constitutionModifier_check_clicked();
    void on_intelligenceModifier_check_clicked();
    void on_wisdomModifier_check_clicked();
    void on_charismaModifier_check_clicked();

private:
    Ui::WizardUI *ui;
	int getModierFromScore(int score);
	void setModifiers(string stats);
    int rolldXX(int xx, int seed);
};

#endif // WIZARDUI_H
