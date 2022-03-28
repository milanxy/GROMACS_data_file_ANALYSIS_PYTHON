
D = load('seqa/output/fort.100');
[Du,D1] = unique(D(:,1));
Dd = diff(D1);
Dr = reshape(D, Dd(1), [], size(D,2));
X = Dr(:,:,1);
Y = Dr(:,:,2);
Z = Dr(:,:,3);
figure(1)

contour(X, Y, Z, 'color', 'black', 'linewidth', 2.0)
set(gca,'XTick',-2:0.5:2,'XTickLabel',-2:0.5:2, 'linewidth', 4.0)
set(gca,'YTick',-2:0.5:2,'YTickLabel',-2:0.5:2, 'linewidth', 4.0)
xlabel({'PC1(nm)'}, 'FontSize',20)
ylabel({'PC2(nm)'}, 'FontSize',20)
a = get(gca,'XTickLabel');  
set(gca,'XTickLabel',a,'fontsize',12,'FontWeight','bold')
set(gca,'XTickLabelMode','auto')
colormap([1,1,1])
%colormap(gray)
hold on

D = load('seqf/output/fort.100');
[Du,D1] = unique(D(:,1));
Dd = diff(D1);
Dr = reshape(D, Dd(1), [], size(D,2));
%X = Dr(:,:,1);
%Y = Dr(:,:,2);
Z = Dr(:,:,3);
contour(X, Y, Z, 'color', 'green', 'linewidth', 2.0)
%colormap([1,1,1])
%[cc,hc]=contourf(X,Y,cIndx,1);
hold on

D = load('seqg/output/fort.100');
[Du,D1] = unique(D(:,1));
Dd = diff(D1);
Dr = reshape(D, Dd(1), [], size(D,2));
%X = Dr(:,:,1);
%Y = Dr(:,:,2);
Z = Dr(:,:,3);
contour(X, Y, Z, 'color', 'blue', 'linewidth', 2.0)
%colormap([1,1,1])
%[cc,hc]=contourf(X,Y,cIndx,1);
hold on

D = load('seqh/output/fort.100');
[Du,D1] = unique(D(:,1));
Dd = diff(D1);
Dr = reshape(D, Dd(1), [], size(D,2));
%X = Dr(:,:,1);
%Y = Dr(:,:,2);
Z = Dr(:,:,3);
contour(X, Y, Z, 'color', 'yellow',  'linewidth', 2.0, 'DisplayName','seq H')
%colormap([1,1,1])
%[cc,hc]=contourf(X,Y,cIndx,1);
hold off
%legend('A','F', 'G','H')
saveas(gcf,'contour_seqafgh.png')
