#ifndef WIZARDUI_H
#define WIZARDUI_H

#include <QMainWindow>

namespace Ui {
class WizardUI;
}

class WizardUI : public QMainWindow
{
    Q_OBJECT

public:
    explicit WizardUI(QWidget *parent = 0);
    ~WizardUI();

private slots:
    void on_pushButton_16_clicked();

    void on_pushButton_15_clicked();

    void on_pushButton_4_clicked();

    void on_pushButton_3_clicked();

    void on_pushButton_6_clicked();

    void on_pushButton_5_clicked();

    void on_pushButton_8_clicked();

    void on_pushButton_7_clicked();

    void on_pushButton_10_clicked();

    void on_pushButton_9_clicked();

private:
    Ui::WizardUI *ui;
};

#endif // WIZARDUI_H
