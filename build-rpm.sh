clear



NAME="x2vnc"
VERSION="1.7.2"
SOURCE_URL="http://fredrik.hubbe.net/x2vnc/${NAME}-${VERSION}.tar.gz"



PWD=`pwd`
BUILD_ROOT="${PWD}/rpmbuild-root"
OUTPUT_DIR="${PWD}"
SPEC_FILE="x2vnc.spec"



BUILD_NUMBER="x"
if [ "$1" == "--build-number" ]; then
	BUILD_NUMBER=${2}
fi



# ensure rpmbuild tool is available
which rpmbuild >/dev/null || { echo "rpmbuild not installed - yum install rpmdevtools"; exit 1; }
# ensure .spec file exists
[[ -f "${SPEC_FILE}" ]] || { echo "Spec file ${SPEC_FILE} not found!"; exit 1; }



# build space
for dir in BUILD RPMS SOURCE SOURCES SPECS SRPMS tmp ; do
	if [ -d "${BUILD_ROOT}/${dir}" ]; then
		rm -rf --preserve-root "${BUILD_ROOT}/${dir}" \
			|| exit 1
	fi
	mkdir -p "${BUILD_ROOT}/${dir}" \
		|| exit 1
done

# copy .spec file
cp "${SPEC_FILE}" "${BUILD_ROOT}/SPECS/" \
	|| exit 1

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
	--define="RELEASE ${BUILD_NUMBER}" \
	"${BUILD_ROOT}/SPECS/${SPEC_FILE}" \
		|| exit 1


