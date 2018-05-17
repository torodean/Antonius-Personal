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

WizardUI::WizardUI(QWidget *parent) : QMainWindow(parent), ui(new Ui::WizardUI){
    ui->setupUi(this);
}

WizardUI::~WizardUI(){
    delete ui;
}

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

//Addition and Subtraction modifier buttons for primary stats.

void WizardUI::on_strengthModifier_plus_clicked(){
    QString levelstr = ui->strengthModifier_main->text();
    int level = levelstr.toInt();
    level++;
    levelstr = QString::number(level);
    ui->strengthModifier_main->setText(levelstr);
}
void WizardUI::on_strengthModifier_minus_clicked(){
    QString levelstr = ui->strengthModifier_main->text();
    int level = levelstr.toInt();
    level--;
    levelstr = QString::number(level);
    ui->strengthModifier_main->setText(levelstr);
}
void WizardUI::on_dexterityModifier_plus_clicked(){
    QString levelstr = ui->dexterityModifier_main->text();
    int level = levelstr.toInt();
    level++;
    levelstr = QString::number(level);
    ui->dexterityModifier_main->setText(levelstr);
}
void WizardUI::on_dexterityModifier_minus_clicked(){
    QString levelstr = ui->dexterityModifier_main->text();
    int level = levelstr.toInt();
    level--;
    levelstr = QString::number(level);
    ui->dexterityModifier_main->setText(levelstr);
}
void WizardUI::on_constitutionModifier_plus_clicked(){
    QString levelstr = ui->constitutionModifier_main->text();
    int level = levelstr.toInt();
    level++;
    levelstr = QString::number(level);
    ui->constitutionModifier_main->setText(levelstr);
}
void WizardUI::on_constitutionModifier_minus_clicked(){
    QString levelstr = ui->constitutionModifier_main->text();
    int level = levelstr.toInt();
    level--;
    levelstr = QString::number(level);
    ui->constitutionModifier_main->setText(levelstr);
}
void WizardUI::on_intelligenceModifier_plus_clicked(){
    QString levelstr = ui->intelligenceModifier_main->text();
    int level = levelstr.toInt();
    level++;
    levelstr = QString::number(level);
    ui->intelligenceModifier_main->setText(levelstr);
}
void WizardUI::on_intelligenceModifier_minus_clicked(){
    QString levelstr = ui->intelligenceModifier_main->text();
    int level = levelstr.toInt();
    level--;
    levelstr = QString::number(level);
    ui->intelligenceModifier_main->setText(levelstr);
}
void WizardUI::on_wisdomModifier_plus_clicked(){
    QString levelstr = ui->wisdomModifier_main->text();
    int level = levelstr.toInt();
    level++;
    levelstr = QString::number(level);
    ui->wisdomModifier_main->setText(levelstr);
}
void WizardUI::on_wisdomModifier_minus_clicked(){
    QString levelstr = ui->wisdomModifier_main->text();
    int level = levelstr.toInt();
    level--;
    levelstr = QString::number(level);
    ui->wisdomModifier_main->setText(levelstr);
}
void WizardUI::on_charismaModifier_plus_clicked(){
    QString levelstr = ui->charismaModifier_main->text();
    int level = levelstr.toInt();
    level++;
    levelstr = QString::number(level);
    ui->charismaModifier_main->setText(levelstr);
}
void WizardUI::on_charismaModifier_minus_clicked(){
    QString levelstr = ui->charismaModifier_main->text();
    int level = levelstr.toInt();
    level--;
    levelstr = QString::number(level);
    ui->charismaModifier_main->setText(levelstr);
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

void WizardUI::setModifiers(){
	QString strength_str = ui->strengthModifier_main->text();
	QString dexterity_str = ui->dexterityModifier_main->text();
	QString constitution_str = ui->constitutionModifier_main->text();
	QString intelligence_str = ui->intelligenceModifier_main->text();
	QString wisdom_str = ui->wisdomModifier_main->text();
	QString charisma_str = ui->charismaModifier_main->text();
	
	int abilities[] = {
		strength.toInt(),
		dexterity.toInt(),
		constitution.toInt(),
		intelligence.toInt(),
		wisdom.toInt(),
		charisma.toInt()
	}

	strength_str = QString::number(getModierFromScore(abilities[0]));
	dexterity_str = QString::number(getModierFromScore(abilities[1]));
	constitution_str = QString::number(getModierFromScore(abilities[2]));
	intelligence_str = QString::number(getModierFromScore(abilities[3]));
	wisdom_str = QString::number(getModierFromScore(abilities[4]));
	charisma_str = QString::number(getModierFromScore(abilities[5]));
	
	ui->strengthModifier_bonus->setText(strength_str);
	ui->dexterityModifier_bonus->setText(dexterity_str);
	ui->constitutionModifier_bonus->setText(constitution_str);
	ui->intelligenceModifier_bonus->setText(intelligence_str);
	ui->wisdomModifier_bonus->setText(wisdom_str);
	ui->charismaModifier_bonus->setText(charisma_str);
}
