#include "wizardui.h"
#include "ui_wizardui.h"

WizardUI::WizardUI(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::WizardUI)
{
    ui->setupUi(this);
}

WizardUI::~WizardUI()
{
    delete ui;
}

void WizardUI::on_pushButton_16_clicked()
{
    QString levelstr = ui->lineEdit_3->text();
    int level = levelstr.toInt();
    level++;
    levelstr = QString::number(level);
    ui->lineEdit_3->setText(levelstr);
}

void WizardUI::on_pushButton_15_clicked()
{
    QString levelstr = ui->lineEdit_3->text();
    int level = levelstr.toInt();
    level--;
    levelstr = QString::number(level);
    ui->lineEdit_3->setText(levelstr);
}

void WizardUI::on_pushButton_4_clicked()
{
    QString levelstr = ui->lineEdit_11->text();
    int level = levelstr.toInt();
    level++;
    levelstr = QString::number(level);
    ui->lineEdit_11->setText(levelstr);
}

void WizardUI::on_pushButton_3_clicked()
{
    QString levelstr = ui->lineEdit_11->text();
    int level = levelstr.toInt();
    level--;
    levelstr = QString::number(level);
    ui->lineEdit_11->setText(levelstr);
}

void WizardUI::on_pushButton_6_clicked()
{
    QString levelstr = ui->lineEdit_14->text();
    int level = levelstr.toInt();
    level++;
    levelstr = QString::number(level);
    ui->lineEdit_14->setText(levelstr);
}

void WizardUI::on_pushButton_5_clicked()
{
    QString levelstr = ui->lineEdit_14->text();
    int level = levelstr.toInt();
    level--;
    levelstr = QString::number(level);
    ui->lineEdit_14->setText(levelstr);
}

void WizardUI::on_pushButton_8_clicked()
{
    QString levelstr = ui->lineEdit_16->text();
    int level = levelstr.toInt();
    level++;
    levelstr = QString::number(level);
    ui->lineEdit_16->setText(levelstr);
}

void WizardUI::on_pushButton_7_clicked()
{
    QString levelstr = ui->lineEdit_16->text();
    int level = levelstr.toInt();
    level--;
    levelstr = QString::number(level);
    ui->lineEdit_16->setText(levelstr);
}

void WizardUI::on_pushButton_10_clicked()
{
    QString levelstr = ui->lineEdit_18->text();
    int level = levelstr.toInt();
    level++;
    levelstr = QString::number(level);
    ui->lineEdit_18->setText(levelstr);
}

void WizardUI::on_pushButton_9_clicked()
{
    QString levelstr = ui->lineEdit_18->text();
    int level = levelstr.toInt();
    level--;
    levelstr = QString::number(level);
    ui->lineEdit_18->setText(levelstr);
}
