Array = csvread('realData.csv');

figure
x = Array(: ,1);
y = Array(: ,3);
z = Array(: ,2);

scatter3(x,y,z)