"""  plotForecasts.py
	Script to plot the various forecast scripts
	Run with e.g. python plotForecasts.py 
	Author:
		Alek Petty

	Update history:
		04/20/2018: Version 1
"""
import matplotlib
matplotlib.use("AGG")

import sys
sys.path.append('../')
import forecast_funcs as ff
from pylab import *



def main(endYear, fmonth, pmonth):
	rawDataPath = '../../Data/' 
	derivedDataPath = '../../DataOutput/'
	saveDataPath=derivedDataPath+'/Arctic/'
	figPath='../../Figures/'+'/Arctic/Predictions/'

	fvars=['conc']
	iceType='extent'
	hemStr='N'
	siiVersion='v3.0'
	startYear=1980
	startYearP=1990
	#endYear=2017
	weight=1
	region=0

	varStrsOut=''.join(fvars)

	forecastVarsM=np.array([]).reshape(0,7)


	for year in range(startYearP, endYear+1):
		outStr='forecastDump'+iceType+varStrsOut+'fm'+str(fmonth)+'pm'+str(pmonth)+'R'+str(region)+str(startYear)+str(year)+'W'+str(weight)+'SII'+siiVersion

		forecastVars=load(saveDataPath+outStr)

		forecastVarsM=np.vstack([forecastVarsM, forecastVars])


	years, extent = ff.get_ice_extentN(rawDataPath, pmonth, startYear, year, 
			icetype=iceType, version=siiVersion, hemStr=hemStr)


	yearsP=np.arange(startYearP, endYear+1)




	"""Plot forecast data """
	rcParams['xtick.major.size'] = 2
	rcParams['ytick.major.size'] = 2
	rcParams['axes.linewidth'] = .5
	rcParams['lines.linewidth'] = .5
	rcParams['patch.linewidth'] = .5
	rcParams['axes.labelsize'] = 8
	rcParams['xtick.labelsize']=8
	rcParams['ytick.labelsize']=8
	rcParams['legend.fontsize']=8
	rcParams['font.size']=7
	rc('font',**{'family':'sans-serif','sans-serif':['Arial']})


	fig = figure(figsize=(3.5,2.2))
	ax1=subplot(1, 1, 1)
	im1 = plot(years, extent, 'k')
	#im2 = plot(Years[start_year_pred-start_year:], lineT[start_year_pred-start_year:]+ExtentG, 'r')

	#im3 = plot(years[-1], extent[-1], marker='o', markersize=2, color='k')
	im3 = plot(yearsP, forecastVarsM[:, 2], marker='x', markersize=1, alpha=0.5, color='k')
	im3 = plot(yearsP, forecastVarsM[:, 3], marker='o', markersize=1, alpha=0.5, color='r')
	ax1.errorbar(yearsP, forecastVarsM[:, 3] , yerr=forecastVarsM[:, 6], color='r',fmt='',linestyle='',alpha=0.5, lw=0.6,capsize=0.5, zorder = 2)

	im3 = plot(yearsP[-1], forecastVarsM[-1, 2], marker='x', markersize=2, color='k')
	im3 = plot(yearsP[-1], forecastVarsM[-1, 3], marker='o', markersize=2, color='r')
	ax1.errorbar(yearsP[-1], forecastVarsM[-1, 3] , yerr=forecastVarsM[-1, 6], color='r',fmt='',linestyle='',lw=0.6,capsize=0.5, zorder = 2)

	#errorbar(YearsP, array(lineTP)+array(ExtentG) , yerr=prederror, color='r',fmt='',linestyle='',lw=0.4,capsize=0.5, zorder = 2)
	#if (np.isfinite(forecastVars[4])):

	#ax1.errorbar(yearsP, extentPredAbs , yerr=[1.96*x for x in perr], color='r',fmt='',linestyle='',lw=0.3,capsize=0.5, zorder = 2)

	forecastStr='%.2f' %(forecastVarsM[-1, 3])
	linearStr='%.2f' %(forecastVarsM[-1, 2])
	observedStr='%.2f' %(extent[-1])

	ax1.annotate('Year: '+str(year)+'\nObserved: '+observedStr+r' M km$^2$'+'\nTrend: '+linearStr+r' M km$^2$',
			xy=(0.7, 1.02), xycoords='axes fraction', horizontalalignment='left', verticalalignment='top')

	ax1.annotate('\nForecast: '+forecastStr+r' M km$^2$',
			xy=(0.7, 0.85), xycoords='axes fraction', color='r', horizontalalignment='left', verticalalignment='top')

	ax1.annotate('June forecasts of September sea ice', fontsize=5, 
			xy=(0.02, 0.02), xycoords='axes fraction', horizontalalignment='left', verticalalignment='bottom')

	ax1.set_ylabel(iceType+r' (Million km$^2$)')
	#ax1.set_xlabel('Years')
	ax1.set_xlim(1980, 2020)
	ax1.set_xticks(np.arange(1980, 2021, 10))
	ax1.set_xticks(np.arange(1980, 2021, 5), minor=True)
	#ax1.set_xticklabels([])
	ax1.set_ylim(3, 8)

	ax1.spines['right'].set_visible(False)
	ax1.spines['top'].set_visible(False)

	plt.tight_layout()
	#subplots_adjust(left=0.15, right=0.90, bottom=0.17, top=0.96, hspace=0)

	savefig(figPath+'/forecast'+outStr+'multi.png', dpi=300)
	close(fig)

#-- run main program
if __name__ == '__main__':
	#main(2015, 6, 9)
	for y in range(1991, 2017+1, 1):
		main(y, 6, 9)


