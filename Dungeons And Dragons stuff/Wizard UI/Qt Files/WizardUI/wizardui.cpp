//============================================================================
// Name        : wizardui.h
// Author      : Antonius Torode
// Date        : 5-17-2018
// Copyright   : This file can be used under the conditions of Antonius' 
//				 General Purpose License (AGPL).
// Description : Used for creating a D&D wizard UI.
//============================================================================

#include "wizardui.h"
#include "ui_wizardui.h"
#include <string>
#include <algorithm>
#include <ctime>
#include <time.h>

using std::string;

int randCounter = 0;

WizardUI::WizardUI(QWidget *parent) : QMainWindow(parent), ui(new Ui::WizardUI){
    ui->setupUi(this);
}

WizardUI::~WizardUI(){
    delete ui;
}

//Updates the level field when the plus or minus boxes next to it are clicked.
void WizardUI::on_levelModifier_plus_clicked(){
    QString levelstr = ui->levelModifier_main->text();
    int level = levelstr.toInt();
    level++;
    levelstr = QString::number(level);
    ui->levelModifier_main->setText(levelstr);
}
void WizardUI::on_levelModifier_minus_clicked(){
    QString levelstr = ui->levelModifier_main->text();
    int level = levelstr.toInt();
    level--;
    levelstr = QString::number(level);
    ui->levelModifier_main->setText(levelstr);
}

//Addition and Subtraction modifier buttons for primary stats. Updates fields accordingly.
void WizardUI::on_strengthModifier_plus_clicked(){
    QString levelstr = ui->strengthModifier_main->text();
    int level = levelstr.toInt();
    level++;
    levelstr = QString::number(level);
    ui->strengthModifier_main->setText(levelstr);
	setModifiers("strength");
}
void WizardUI::on_strengthModifier_minus_clicked(){
    QString levelstr = ui->strengthModifier_main->text();
    int level = levelstr.toInt();
    level--;
    levelstr = QString::number(level);
    ui->strengthModifier_main->setText(levelstr);
	setModifiers("strength");
}
void WizardUI::on_dexterityModifier_plus_clicked(){
    QString levelstr = ui->dexterityModifier_main->text();
    int level = levelstr.toInt();
    level++;
    levelstr = QString::number(level);
    ui->dexterityModifier_main->setText(levelstr);
	setModifiers("dexterity");
}
void WizardUI::on_dexterityModifier_minus_clicked(){
    QString levelstr = ui->dexterityModifier_main->text();
    int level = levelstr.toInt();
    level--;
    levelstr = QString::number(level);
    ui->dexterityModifier_main->setText(levelstr);
	setModifiers("dexterity");
}
void WizardUI::on_constitutionModifier_plus_clicked(){
    QString levelstr = ui->constitutionModifier_main->text();
    int level = levelstr.toInt();
    level++;
    levelstr = QString::number(level);
    ui->constitutionModifier_main->setText(levelstr);
	setModifiers("constitution");
}
void WizardUI::on_constitutionModifier_minus_clicked(){
    QString levelstr = ui->constitutionModifier_main->text();
    int level = levelstr.toInt();
    level--;
    levelstr = QString::number(level);
    ui->constitutionModifier_main->setText(levelstr);
	setModifiers("constitution");
}
void WizardUI::on_intelligenceModifier_plus_clicked(){
    QString levelstr = ui->intelligenceModifier_main->text();
    int level = levelstr.toInt();
    level++;
    levelstr = QString::number(level);
    ui->intelligenceModifier_main->setText(levelstr);
	setModifiers("intelligence");
}
void WizardUI::on_intelligenceModifier_minus_clicked(){
    QString levelstr = ui->intelligenceModifier_main->text();
    int level = levelstr.toInt();
    level--;
    levelstr = QString::number(level);
    ui->intelligenceModifier_main->setText(levelstr);
	setModifiers("intelligence");
}
void WizardUI::on_wisdomModifier_plus_clicked(){
    QString levelstr = ui->wisdomModifier_main->text();
    int level = levelstr.toInt();
    level++;
    levelstr = QString::number(level);
    ui->wisdomModifier_main->setText(levelstr);
	setModifiers("wisdom");
}
void WizardUI::on_wisdomModifier_minus_clicked(){
    QString levelstr = ui->wisdomModifier_main->text();
    int level = levelstr.toInt();
    level--;
    levelstr = QString::number(level);
    ui->wisdomModifier_main->setText(levelstr);
	setModifiers("wisdom");
}
void WizardUI::on_charismaModifier_plus_clicked(){
    QString levelstr = ui->charismaModifier_main->text();
    int level = levelstr.toInt();
    level++;
    levelstr = QString::number(level);
    ui->charismaModifier_main->setText(levelstr);
	setModifiers("charisma");
}
void WizardUI::on_charismaModifier_minus_clicked(){
    QString levelstr = ui->charismaModifier_main->text();
    int level = levelstr.toInt();
    level--;
    levelstr = QString::number(level);
    ui->charismaModifier_main->setText(levelstr);
	setModifiers("charisma");
}

//Update button for ability scores.
void WizardUI::on_abilityModifier_all_clicked(){
	setModifiers("all");
}

//Sets the modifier field based on the ability score.
int WizardUI::getModierFromScore(int score){
	if(score == 1){
		return -5;
	} else if (score <= 3){
		return -4;
	} else if (score <= 5){
		return -3;
	} else if (score <= 7){
		return -2;
	} else if (score <= 8){
		return -1;
	} else if (score <= 11){
		return 0;
	} else if (score <= 13){
		return 1;
	} else if (score <= 15){
		return 2;
	} else if (score <= 17){
		return 3;
	} else if (score <= 19){
		return 4;
	} else if (score <= 21){
		return 5;
	} else if (score <= 23){
		return 6;
	} else if (score <= 25){
		return 7;
	} else if (score <= 27){
		return 8;
	} else if (score <= 29){
		return 9;
	} else if (score == 30){
		return 10;
	}
}
void WizardUI::setModifiers(string stats){
	if(stats == "all"){ //updates all ability stats.
		QString strength_str = ui->strengthModifier_main->text();
		QString dexterity_str = ui->dexterityModifier_main->text();
		QString constitution_str = ui->constitutionModifier_main->text();
		QString intelligence_str = ui->intelligenceModifier_main->text();
		QString wisdom_str = ui->wisdomModifier_main->text();
		QString charisma_str = ui->charismaModifier_main->text();
		
		//converts the QStrings to ints.
		int abilities[] = {
            strength_str.toInt(), dexterity_str.toInt(), constitution_str.toInt(),
            intelligence_str.toInt(), wisdom_str.toInt(), charisma_str.toInt()
        };

		//Determines the modifiers for each stat and stores it as a QString.
		strength_str = QString::number(getModierFromScore(abilities[0]));
		dexterity_str = QString::number(getModierFromScore(abilities[1]));
		constitution_str = QString::number(getModierFromScore(abilities[2]));
		intelligence_str = QString::number(getModierFromScore(abilities[3]));
		wisdom_str = QString::number(getModierFromScore(abilities[4]));
		charisma_str = QString::number(getModierFromScore(abilities[5]));
		
		//Updates the ui with the modifiers.
		ui->strengthModifier_bonus->setText(strength_str);
		ui->dexterityModifier_bonus->setText(dexterity_str);
		ui->constitutionModifier_bonus->setText(constitution_str);
		ui->intelligenceModifier_bonus->setText(intelligence_str);
		ui->wisdomModifier_bonus->setText(wisdom_str);
		ui->charismaModifier_bonus->setText(charisma_str);
		
	} else if (stats == "strength"){ //updates only the strength stat.
		QString strength_str = ui->strengthModifier_main->text();
        int ability = strength_str.toInt();
        strength_str = QString::number(getModierFromScore(ability));
		ui->strengthModifier_bonus->setText(strength_str);
		
	} else if (stats == "dexterity"){ //updates only the dexterity stat.
		QString dexterity_str = ui->dexterityModifier_main->text();
        int ability = dexterity_str.toInt();
        dexterity_str = QString::number(getModierFromScore(ability));
		ui->dexterityModifier_bonus->setText(dexterity_str);
		
	} else if (stats == "constitution"){ //updates only the constitution stat.
		QString constitution_str = ui->constitutionModifier_main->text();
        int ability = constitution_str.toInt();
        constitution_str = QString::number(getModierFromScore(ability));
		ui->constitutionModifier_bonus->setText(constitution_str);
		
	} else if (stats == "intelligence"){ //updates only the intelligence stat.
		QString intelligence_str = ui->intelligenceModifier_main->text();
        int ability = intelligence_str.toInt();
        intelligence_str = QString::number(getModierFromScore(ability));
		ui->intelligenceModifier_bonus->setText(intelligence_str);
		
	} else if (stats == "wisdom"){ //updates only the wisdom stat.
		QString wisdom_str = ui->wisdomModifier_main->text();
        int ability = wisdom_str.toInt();
        wisdom_str = QString::number(getModierFromScore(ability));
		ui->wisdomModifier_bonus->setText(wisdom_str);
		
	} else if (stats == "charisma"){ //updates only the charisma stat.
		QString charisma_str = ui->charismaModifier_main->text();
        int ability = charisma_str.toInt();
        charisma_str = QString::number(getModierFromScore(ability));
		ui->charismaModifier_bonus->setText(charisma_str);
	}
}

void WizardUI::on_strengthModifier_check_clicked(){
    QString strength_str = ui->strengthModifier_bonus->text();
    int ability = strength_str.toInt();
    int roll = rolldXX(20,randCounter) + ability;
    randCounter++;
    ui->ability_saving_throw->setText(QString::number(ability));
}

void WizardUI::on_dexterityModifier_check_clicked(){
	QString dexterity_str = ui->dexterityModifier_bonus->text();
    int ability = strength_str.toInt();
    int roll = rolldXX(20,randCounter) + ability;
    randCounter++;
    ui->ability_saving_throw->setText(QString::number(roll));
}

void WizardUI::on_constitutionModifier_check_clicked(){
	QString constitution_str = ui->constitutionModifier_bonus->text();
    int ability = strength_str.toInt();
    int roll = rolldXX(20,randCounter) + ability;
    randCounter++;
    ui->ability_saving_throw->setText(QString::number(roll));
}

void WizardUI::on_intelligenceModifier_check_clicked(){
	QString intelligence_str = ui->intelligenceModifier_bonus->text();
    int ability = strength_str.toInt();
    int roll = rolldXX(20,randCounter) + ability;
    randCounter++;
    ui->ability_saving_throw->setText(QString::number(roll));
}

void WizardUI::on_wisdomModifier_check_clicked(){
	QString wisdom_str = ui->wisdomModifier_bonus->text();
    int ability = strength_str.toInt();
    int roll = rolldXX(20,randCounter) + ability;
    randCounter++;
    ui->ability_saving_throw->setText(QString::number(roll));
}

void WizardUI::on_charismaModifier_check_clicked(){
	QString charisma_str = ui->charismaModifier_bonus->text();
    int ability = strength_str.toInt();
    int roll = rolldXX(20,randCounter) + ability;
    randCounter++;
    ui->ability_saving_throw->setText(QString::number(roll));
}

//Returns a random integer between min and max.
int randomInt(int min, int max, int seed, bool useTime){
    if(max < min){
        return min;
    }
    if(seed == 0){
        srand((unsigned)time(0));
    } else if (useTime){
        srand((unsigned)time(0) + seed);
    } else {
        srand(seed);
    }
    int random = min + (rand() % static_cast<int>(max - min + 1));
    return random;
}

//returns a 1dXX output.
int WizardUI::rolldXX(int xx, int seed){
    return randomInt(1,xx,seed,true);
}
