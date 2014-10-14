


NAME="x2vnc"
VERSION="1.7.2"
SOURCE_URL="http://fredrik.hubbe.net/x2vnc/${NAME}-${VERSION}.tar.gz"
SPEC_FILE="x2vnc.spec"



# load build_utils.sh script
if [ -e build_utils.sh ]; then
	source ./build_utils.sh
elif [ -e /usr/local/bin/pxn/build_utils.sh ]; then
	source /usr/local/bin/pxn/build_utils.sh
else
	wget https://raw.githubusercontent.com/PoiXson/shellscripts/master/pxn/build_utils.sh \
		|| exit 1
	source ./build_utils.sh
fi



# get source file
if [ ! -f "${BUILD_ROOT}/SOURCES/${NAME}-${VERSION}.tar.gz" ]; then
	if [ ! -f "${PWD}/${NAME}-${VERSION}.tar.gz" ]; then
		wget -O "${PWD}/${NAME}-${VERSION}.tar.gz" "${SOURCE_URL}" \
			|| { echo "Failed to download source!"; exit 1; }
	fi
	cp "${PWD}/${NAME}-${VERSION}.tar.gz" "${BUILD_ROOT}/SOURCES" \
		|| exit 1
fi



# build rpm
rpmbuild -ba \
	--define="_topdir ${BUILD_ROOT}" \
	--define="_tmppath ${BUILD_ROOT}/tmp" \
	--define="_rpmdir ${OUTPUT_DIR}" \
	--define="_srcrpmdir ${OUTPUT_DIR}" \
	--define="BUILD_NUMBER ${BUILD_NUMBER}" \
	"${BUILD_ROOT}/SPECS/${SPEC_FILE}" \
		|| exit 1

